
# The Process class represents a process in our system.

# When we print processes, we will print them in json format
import json

class Process:

    # Contructor - the default values for the member variables
    # are as indicated - an empty string for the process name,
    # and -1 for the process id
    #
    # TODO: 
    # Add the new attributes. Always initialize cpu_used to 0
    def __init__(self, process_name="", process_id=-1):
        self.process_name = process_name
        self.process_id = process_id

    
    # Set the process name 
    def setProcessName(self, process_name):
        self.process_name = process_name

    # Set the process ID
    def setProcessId(self, process_id):
        self.process_id = process_id

    # get the process name
    def processName(self):
        return self.process_name
    
    # get the process id
    def processId(self):
        return self.process_id


    # TODO:
    # Add setters and getters for the new
    # attributes (priority and cpu_needed)


    # TODO:
    # Add a getter (but not a setter) for cpu_used
    


    def run(self, num_cycles):
        # TODO:
        # Impmlement the run() method.
        #
        # Determine how many cycles the process should actually execute
        # (that number should either be the value of numCycles provided,
        # or a smaller number if the process doesn't need that many cycles)
        #
        # Update cpu_used to reflect the actual number of cycles executed, 
        # and return the number executed.



    # This method is called when print() is called. 
    # It converts the contents of the object
    # to json, and then dumps the json format. 
    #
    # TODO: 
    # Add the new attributes, including cpu_used
    def __str__(self):
        return json.dumps({"process_name" : self.process_name,
                           "process_id" : self.process_id, 
                           separators = (",",":"), sort_keys = True)
