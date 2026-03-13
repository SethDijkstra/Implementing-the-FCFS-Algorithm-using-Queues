# This file defines two classes: Process and FCFSAlgorithm.
# A Process represents a single task waiting to be run by the CPU.
# FCFSAlgorithm runs those processes in the order they arrived (First-Come, First-Served).

from node_queue import NodeQueue


# process class - holds all the info about one process
class Process:

    # constructor
    def __init__(self, process_id, arrival_time, burst_time):
        # store the basic process info
        self.process_id = process_id
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        # these get calculated later in the algorithm
        self.waiting_time = 0
        self.turnaround_time = 0

    def __str__(self):
        # just a nice way to print process info
        return (f"Process {self.process_id} | "
                f"Arrival: {self.arrival_time} | "
                f"Burst: {self.burst_time} | "
                f"Waiting: {self.waiting_time} | "
                f"Turnaround: {self.turnaround_time}")


# FCFS scheduler class
class FCFSAlgorithm:

    def __init__(self):
        # queue to hold all the processes
        self.process_queue = NodeQueue()
        # also keep a list so we can print results at the end
        self.all_processes = []

    # adds a process to the queue
    def add_process(self, new_process):
        self.process_queue.enqueue(new_process)
        self.all_processes.append(new_process)

    # runs the actual FCFS simulation
    def run(self):
        current_time = 0  # keeps track of what time it is

        while not self.process_queue.is_empty():
            # grab the next process from the queue
            process = self.process_queue.dequeue()

            # if the cpu is idle waiting for the next process to arrive
            if current_time < process.arrival_time:
                current_time = process.arrival_time

            # waiting time = how long it waited before cpu picked it up
            process.waiting_time = current_time - process.arrival_time

            # now run the process
            current_time += process.burst_time

            # turnaround = total time from when it arrived to when it finished
            process.turnaround_time = current_time - process.arrival_time

    # returns average waiting time
    def get_average_waiting_time(self):
        total = 0
        for p in self.all_processes:
            total += p.waiting_time
        return total / len(self.all_processes)

    # returns average turnaround time
    def get_average_turnaround_time(self):
        total = 0
        for p in self.all_processes:
            total += p.turnaround_time
        return total / len(self.all_processes)