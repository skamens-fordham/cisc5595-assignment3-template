# CISC 5595 Assignment 3: Process Scheduling

In this assignment, we will enhance our Process class so that we can simulate a "running" process. We will then implement a number of different CPU scheduling algorithms using this capability.

# Process class

We will start with our Process and ProcessTable classes from Assignment 2, and add to them for this assignment.

## Copy files from assignment 2
Copy the following files from your assignment 2 directory/repository into this directory:

  * `process.h`
  * `process.cpp`
  * `process_table.h`
  * `process_table.cpp`
  * `process_test.cpp`

## Add files to the git repository
Add these files to the git repository using the following commands:

``` 
$ git add process.h process.cpp process_table.h process_table.cpp process_test.cpp
$ git commit --message "Add Process and ProcessTable files to repo" 
```
## Changes to the Process class

We will need to make a number of changes to the Process class for this project, as follows:

### Add new attributes

Add the following new attributes to your Process class:

* `priority` - an integer value representing the scheduling priority of the process, where 0 repesents the highest priority. Assume that the default "standard-user" priority is 100.
* `cpu_needed` - the number of cpu cycles the process needs to run over its entire lifetime
* `cpu_used` - the number of cpu cycles that have actually executed for the process. This will be an internal attribute of the object.

Update your `Process` class as follows:
* Update your constructor so you can specify the new attributes at object creation time
* Add appropriate set and get methods for these attributes
* Update the to_json and from_json methods to take the new attributes into account
* Update your print methods to display them

### Add `run` method

Add a new method to your Process class called `run`. Its function signature should be as follows:

`int run(int numCycles)`

The `run` method should behave as follows:

* The `numCycles` parameter indicates how many CPU cycles the process is allowed to use
* Calculate how many CPU cycles the process will actually use
* Update the `cpu_used` member to indicate how many cycles have been used overall
* Return the actual number of cycles used (which could be less than the value of the `numCycles` parameter)

### Add tests
Add new tests in `process_test.cpp` to verify the new code.

# CPU Scheduler Classes

You will implement two different scheduling algorithms for this assignment, based on the instructions below.

## Base Class

The starter files contain a file `cpu_scheduler_base.h` which defines an [Abstract Base Class](https://www.tutorialspoint.com/cplusplus/cpp_interfaces.htm) for our schedulers. This base class requires that any class derived from it must implement the following two methods:
* `virtual bool addProcess(Process& process)`
* `virtual bool removeProcess(Process& process)`
* `virtual Process& nextProcess()`

See the comments in `cpu_scheduler_base.h` for details on the class's expected behavior.

## First Come, First-Served Scheduler

There will be a starter header file in your directory called `cpu_scheduler_fcfs.h` which will contain the declaration of your First-Come, First-Served scheduler class. Add a new file `cpu_scheduler_fcfs.cpp` to contain your implementation of this class. Add the new file to your repository using `git add`, and update your Makefile to build it.

Based on the instructions in the header file, implement this scheduler class in these files.

## Priority round-robin scheduler

There will be a starter header file in your directory called `cpu_scheduler_priority_rr.h` which will contain the declaration of your Priority Round-Robin scheduler class. Add a new file `cpu_scheduler_priority_rr.cpp` to contain your implementation of this class. Add the new file to your repository using `git add`, and update your Makefile to build it.

Based on the instructions in the header file, implement this scheduler class in these files.

# run_processes

`run_processes` is the main program that you will use to exercise your scheduling algorithms. The program will take the desired scheduling algorithm as a command line argument along with a set of json files defining the processes that should be run.

It will simulate running all of the processes from the input files.

Follow the comments in `run_processes.cpp` to implement and test this program  



