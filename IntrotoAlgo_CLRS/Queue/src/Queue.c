/*
 ============================================================================
 Name        : Queue.c
 Author      : Angelo
 Version     :
 Copyright   : Your copyright notice
 Description : Hello World in C, Ansi-style
 ============================================================================
 */

#include <stdio.h>
#include <stdlib.h>
#include "stdint.h"
#include "dxcm_ptr_q.h"
#include "scheduler.h"

static void taskA()
{
	puts("Executing Task A!!! \n");
}

static void taskB()
{
	puts("Executing Task B!!! \n");
}
static void taskC()
{
	puts("Executing Task C!!! \n");
}
static void taskD()
{
	puts("Executing Task D!!! \n");
}

int main(void) {

	initDxcmScheduler();

	printf("Task A Address: %p \n",&taskA);
	printf("Task B Address: %p \n",&taskB);
	printf("Task C Address: %p \n",&taskC);
	printf("Task D Address: %p \n",&taskD);

	sched_cb calbk;

	calbk = &taskD;
	scheduleDxcmTask(calbk,2);
	calbk = &taskC;
	scheduleDxcmTask(calbk,3);
	calbk = &taskA;
	scheduleDxcmTask(calbk,0);
	calbk = &taskB;
	scheduleDxcmTask(calbk,1);

	puts("******Executing Task Scheduler\n");
	executeDxcmScheduler();
	puts("******End Executing Task Scheduler\n");

	calbk = &taskD;
	calbk();
	calbk = &taskC;
	calbk();
	calbk = &taskA;
	calbk();
	calbk = &taskB;
	calbk();

	/*
	static uint8_t mempool[Q_REQUIRED_MEM_SIZE(10)];

	uint64_t ptr = 0;

	printf("Required Mem Size: %u \n",Q_REQUIRED_MEM_SIZE(10));
	printf("Initializing Queue \n");
	static q_t current;
	current = q_init(mempool,Q_REQUIRED_MEM_SIZE(10));
	uint8_t ptrArray[15] = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15};
	for(int32_t index = 0; index<5; index++)
	{
		printf("Queue element 			: %d \n",*(ptrArray+index));
		printf("Queue element Address	: %u \n",(ptrArray+index));

		q_enqueue(current,ptrArray+index);
	}

	//printQ
	for(int32_t index = current->head; index<current->size; index++)
	{
		printf("Print Queue element 			: %d \n",(*(uint8_t*)(current->ptrs[0+index])));
		printf("Print Queue element Address	: %u \n",(current->ptrs[0+index]));
	}

	for(int32_t index = 5; index<10; index++)
	{
		printf("Queue element 			: %d \n",*(ptrArray+index));
		printf("Queue element Address	: %u \n",(ptrArray+index));

		q_enqueue(current,ptrArray+index);
	}

	printf("ptr value for Dequeue: %u, %u \n",ptr,&ptr);

	for(int32_t index = 0; index<5; index ++)
	{
	    printf("Print Current Q address				:%d\n",current);
		printf("Dequeue Successful? %d \n",q_dequeue(current,&ptr));
//		printf("dequeued element is: %d \n",*ptr);
	}
	//Q_REQUIRED_MEM_SIZE(10);

	 */
	puts("!!!Hello World!!!");
	return EXIT_SUCCESS;
}
