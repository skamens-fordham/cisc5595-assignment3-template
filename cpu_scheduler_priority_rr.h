#ifndef CISC5595_CPU_SCHEDULER_PRIORITY_RR_H
#define CISC5595_CPU_SCHEDULER_PRIORITY_RR_H

// cpu_scheduler_priority_rr.h
//
// Abstract base class of a CPU scheduler.

#include "process.h"
#include "cpu_scheduler_base.h"

class CpuSchedulerPriorityRoundRobin : public CpuSchedulerBase {

    public:

        // Add a new process to the set of processes to be
        // scheduled.
        virtual bool addProcess(Process process);
        
        // Remove a process from the scheduler (generally
        // because it's done).
        virtual bool removeProcess(Process process);

        // Get the process id of the next process to be scheduled
        // If no processes remain to schedule, return -1
        virtual int nextProcess();

    private:
        // Define a data structure that will hold the
        // process ID's that have been added to the scheduler
        // and will help to implement the scheduling algorithm
	
};

#endif // CISC5595_CPU_SCHEDULER_PRIORITY_RR_H

