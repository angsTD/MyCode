/*
 * scheduler.h
 *
 *  Created on: Feb 20, 2017
 *      Author: Angelo
 */

#ifndef SCHEDULER_H_
#define SCHEDULER_H_

#include "stdint.h"

typedef void (*sched_cb)(void);

void initDxcmScheduler(void);

int32_t scheduleDxcmTask(sched_cb clbk, uint8_t priority);

void executeDxcmScheduler(void);

#endif /* SCHEDULER_H_ */
