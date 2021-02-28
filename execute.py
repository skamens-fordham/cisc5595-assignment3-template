#!/usr/bin/python3

from process import Process
from process_table import ProcessTable
from cpu_scheduler_fcfs import CpuSchedulerFcfs
from cpu_scheduler_priorty_rr import CpuSchedulerPriorityRoundRobin

import json
import sys

def main():

    
    # Validate the command line

    if (len(sys.argv) != 2) :
        sys.exit("Usage: " + sys.argv[0] + " <input file>")

    input = {}

    # Load the input file into the json object
    with open(sys.argv[1]) as f:
        input = json.load(f)

    # Initialize the table size to the default
    # of 100
    table_size = 100    

    # Read the table size from "options"
    if 'options' in input:
        options = input['options']
        if 'table_size' in options:
            table_size = options['table_size']

    # Initialize the process table with the given size
    table = ProcessTable(table_size)


    # Initialize an empty scheduler object.
    scheduler = None
    algorithm = ''

    # TODO:
    # Determine the scheduling algorithm from the schedule
    # segment. If the scheduling algorithm in not found
    # in the input, or if the value is not 
    # one of "fcfs" or "priority_round_robin" 
    # exit with an error

    
    # Initialize the scheduler object (see above)
    # With an object of the type indicated by the 
    # algorithm
    if algorithm == 'fcfs' :
        scheduler = CpuSchedulerFcfs()
    elif algorithm == 'priority_round_robin':
        scheduler = CpuSchedulerPriorityRoundRobin()
    


    # Scheduling quantum defaults to 1 if it is not specified in the
    # input
    scheduling_quantum = 1

    # TODO:
    # If "scheduling_quantum" is in the "schedule" segment, 
    # retrieve its value. Validate that the value is greater than 0.
    # If an incorrect value is provided, exit with an error.


    
    # TODO: 
    # Iterate the "processes" list in the input json.
    # Add each process in the list to *both* the process
    # table and the scheduler.



    # Print the process table one time after all processes are loaded
    print(table, "\n")


    # TODO: 
    # Execute the scheduling algorithm in a loop.
    # The basic sequence is:
    # 1. Get the process ID of the next process that should be run
    # 2. Find that process in the ProcessTable
    # 3. Call that process's run() method, making sure to 
    #    tell it how many cycles to execute.
    # 4. Print the entire process table
    # 5. If the process that you just ran has used up all of the
    #    CPU that it needed, remove it from the process table
    #    and the scheduler
    #
    # The loop should end when there are no longer any processes to schedule



    return 0

if __name__ == "__main__":
    main()
