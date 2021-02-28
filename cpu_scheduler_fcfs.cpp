#include "cpu_scheduler_fcfs.h"
#include "process.h"

bool CpuSchedulerFcfs::addProcess(Process process)
{
   // TODO:
   // Add a process to be scheduled.

   // Return true if the process was successfully added,
   // and false otherwise
}

// Remove a process from the scheduling queue
bool CpuSchedulerFcfs::removeProcess(Process process)
{
    // TODO: 
    // Remove a process from the scheduler. 
    // If the process was successfully removed,
    // return true; otherwise, if the process
    // wasn't found in the schedule, return false.

}

// Find the next process to run
int CpuSchedulerFcfs::nextProcess()
{
   // TODO: 
   // Return the process ID of the next process
   // that should be executed.
   //
   // If there are no processes remaining to 
   // schedule, return -1
}
