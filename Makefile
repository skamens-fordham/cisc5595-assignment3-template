CPPFLAGS = -g -I.

libsrc = process.cpp process_table.cpp
libobj = $(libsrc:.cpp=.o)

all: process_test run_processes $(libobj)

process_test: process_test.o $(libobj)
	$(CXX) -o $@ process_test.o $(LDFLAGS) $(libobj)

run_processes: run_processes.o $(libobj)
	$(CXX) -o $@ run_processes.o $(libobj)

.PHONY: clean
clean:
	rm -f process_test process_test.o run_processes run_processes.o $(libobj)