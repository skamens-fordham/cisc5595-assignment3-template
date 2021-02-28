# Implements a CPU scheduling class using the priority round-robin
# algorithm.

from process import Process

class CpuSchedulerPriorityRoundRobin:
    def __init__(self):
        # TODO: 
        # Add a data structure here that will hold the processes
        # that need to be scheduled. Note that since you need to schedule 
        # in order of priority, you will need to store both the priority
        # and the process ID of each process.
        # Initialize this data structure here

    
    # Add a process to the queue
    def addProcess(self, p):
        # TODO:
        # Add a process to be scheduled.

        # The processes should be stored in such a way that
        # all processes of the same priority are grouped together, 
        # and a new process is added to the end of the list for a 
        # particular priority.

        # Return true if the process was successfully added,
        # and false otherwise.

    def removeProcess(self, p):
        # TODO: 
        # Remove a process from the scheduler. 

        # If the process was successfully removed,
        # return True; otherwise, if the process
        # wasn't found in the schedule, return False.

    def nextProcess(self):
        # TODO: 
        # Return the process ID of the next process
        # that should be executed.
        #
        # The next process to be executed should always 
        # be a process that has the highest priority of the
        # ones remaining in the scheduler.
        #
        # If there is more than one process at the highest priority,
        # these processes should be scheduled in a round-robin fashion,
        # so each of the processes at the highest priority gets
        # to run in turn until they are all complete.
        #
        # If there are no processes remaining to 
        # schedule, return -1        


