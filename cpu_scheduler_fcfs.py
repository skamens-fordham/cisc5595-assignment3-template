# Implements a CPU scheduling class using the first-come, first-served
# algorithm.

from process import Process

class CpuSchedulerFcfs:
    def __init__(self):
        # TODO: 
        # Determine the appropriate data structure to use to store your
        # processes to be scheduled. Initialize that data structure
        # here.

    
    # Add a process
    def addProcess(self, p):
        # TODO: 
        # Add a process to be scheduled.

        # Return True if the process was successfully added,
        # and False otherwise

    # Remove a process from the scheduler
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
        
        # If there are no processes remaining to 
        # schedule, return -1       
