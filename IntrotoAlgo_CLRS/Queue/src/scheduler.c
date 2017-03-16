/*
 * scheduler.c
 *
 *  Created on: Feb 20, 2017
 *      Author: Angelo
 */


#include "stdint.h"
#include "dxcm_ptr_q.h"
#include "scheduler.h"
#include <stdio.h>

const uint32_t NUM_OF_PRIORITIES = 5;

uint8_t _mem[NUM_OF_PRIORITIES][Q_REQUIRED_MEM_SIZE(10)] __attribute__ ((aligned(4)));
q_t q[NUM_OF_PRIORITIES];

sched_cb clbck;

void initDxcmScheduler()
{
    for(uint8_t index = 0; index< NUM_OF_PRIORITIES; index++)
    {
        q[index] = q_init(_mem[index], sizeof(_mem[index]));
    }
}

int32_t scheduleDxcmTask(sched_cb clbk, uint8_t priority)
{
    if(priority >= NUM_OF_PRIORITIES) return -1;

    return q_enqueue(q[priority],(void*)clbk);
}

void executeDxcmScheduler()
{
    do
    {
        for(uint32_t prior = 0; prior < NUM_OF_PRIORITIES; prior++)
        {
            printf("Executing Queue with Priority: %u\n",prior);
        	clbck = NULL;
        	uint64_t ptr = 0;
            q_dequeue(q[prior],&ptr);
            clbck = (sched_cb)(ptr);
            printf("clbk and ptr: (%p,%p)\n",clbck,ptr);
            if(clbck)
            {
            	printf("Task Address: %p \n",ptr);
            	clbck();
                break;
            }
        }

    }while(clbck);
}
