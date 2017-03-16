/*
    Dexcom FIFO pointer Queue
*/
#include "dxcm_ptr_q.h"
#include <stdio.h>

/* Here we provide details to the compiler about what structure contains */
//typedef struct q_private_t
//{
//  unsigned tail; /* Position at which to insert the next q element */
//  unsigned head; /* Position at which element can be dequeued */
//  unsigned capacity; /* Maximum number of elements which can be stored */
//  unsigned size; /* Number of elements in the queue right now */
//  void*    ptrs[1]; /* array of pointers follows the header information.
//                       Array must contain at least 1 element but we will
//                       index past this if additional memory is provided */
//} q_obj_t;

//#define Q_REQUIRED_MEM_SIZE(num) (sizeof(q_obj_t) + num*sizeof(void*))

unsigned q_overhead_bytes(void)
{
    return sizeof(q_obj_t);
}

q_t q_init(void* memory, unsigned size)
{
    if (!memory) return NULL;
    if ((uint32_t)memory & 3) return NULL;

    if (size < (sizeof(q_obj_t))) return NULL;

    q_obj_t *q = (q_obj_t*)memory;
    size -= (sizeof(*q) - sizeof(q->ptrs)); /* Remove most of the header from the
                                             provided memory. q->ptrs __is__ the
                                             rest of the memory */
    q->tail = q->head = q->size = 0;
    q->capacity = size / sizeof(void*);

    return q;
}

int q_enqueue(q_t q, void* ptr)
{
    if (q->size == q->capacity) return -1;
    q->ptrs[(q->tail)++] = ptr;

    if (q->tail == q->capacity) q->tail = 0;
    q->size += 1;
    printf("Print Queue element Head				:%d\n",q->head);
    return 0;
}

void* q_dequeue(q_t q, void *ptr)
{
    printf("DeQueue started	\n");
    printf("Print DeQueue element Head				:%d\n",q->head);
    if (!q) return 0;
    if (!q->size) return 0;

    printf("Print DeQueue (Index,Value) 			: (%d,%p) \n",q->head,(q->ptrs[q->head]));
//    void* ptr = 0;
    *(uint64_t*)ptr = q->ptrs[(q->head)++];

    if (q->head == q->capacity) q->head = 0;
    q->size -= 1;

    return ptr;
}

/*
obj_t* queue_init(void* mem,uint32_t size)
{
    obj_t *Q = (obj_t*)mem;
    Q->capacity = (size-sizeof(*Q))/sizeof(void*);
//    Q->ptrs = Q+1;
    Q->head = 0;
    Q->tail = 0;
    return Q;
}

int enqueue(obj_t* Q,void *ptr)
{
    if(Q->size == Q->capacity) return -1;

    (Q->ptrs)[(Q->tail)++] = ptr;

    if(Q->tail == Q->size)
    {
        Q->tail = 0;
    }

    Q->size++;

    return 0;
}

int dequeue(obj_t* Q, void *ptr)
{
    if(!(Q->size)) //Empty Queue
    {
        return -1;
    }

    ptr = (Q->ptrs[Q->head++]);

    if(Q->head == Q->capacity)
    {
        Q->head = 0;
    }

    Q->size--;

    return 0;
}
*/
