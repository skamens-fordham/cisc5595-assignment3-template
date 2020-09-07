// Main program for assignment 3 - Process Scheduling
//
// This program will be run as follows:
//
// run_processes --algorithm=<algo> <json_files>
//    Where <algo> will be either "fcfs" or "priority", and
//          <json_files> is a set of one or more processes to run

#include "cpu_scheduler_base.h"
#include "cpu_scheduler_fcfs.h"
#include "cpu_scheduler_priority_rr.h"
#include "process.h"
#include "process_table.h"

#include <iostream>

using namespace std;




int main(int argc, char ** argv)
{
    ProcessTable table;             // Will contain the processes to be scheduled
    CpuSchedulerBase * scheduler;   // Scheduler that will be used 
    string algorithm;               // String choosing which scheduling algorithm to use

    // Use getopt_long to process the command line arguments.
    // If the algorithm argument is missing, the program
    // should fail.


    // Allocate a scheduling object based on the
    // chosen algorithm.
    if (algorithm == "fcfs") {
        scheduler = (CpuSchedulerBase *) new CpuSchedulerFcfs;
    } else if (algorithm == "priority") {
        scheduler = (CpuSchedulerBase *) new CpuSchedulerPriorityRoundRobin;
    }

    // Load the processes from the input files into the process table
    // This should use the same code you used for load_table in assignment 2




    // Iterate the set of processes in the ProcessTable and add
    // each process to the scheduler. Processes should be added 
    // in order of process_id, from 1 to the maximum table size



    // Run a loop to schedule one CPU cycle for each process
    // as long as there are still processes to schedule.
    //
    // Each time a process runs, output a line of the following format:
    //
    //     <process_name>(<priority>): <total_cpu_cycles_so_far>/<total_cpu_needed>
    //
    // So if there is only one process called "process1" with priority 10 that needs 3
    // total CPU cycles, we would expect to see the following output:
    //
    // process1(10): 1/3
    // process1(10): 2/3
    // process1(10): 3/3
}