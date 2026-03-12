# This file defines two classes: Process and FCFSAlgorithm.
# A Process represents a single task waiting to be run by the CPU.
# FCFSAlgorithm runs those processes in the order they arrived (First-Come, First-Served).
#
# TODO: Implement the Process and FCFSAlgorithm classes.
# Process should store process_id, arrival_time, burst_time, waiting_time, turnaround_time.
# FCFSAlgorithm should use a queue to manage processes and calculate times.

from node_queue import NodeQueue


# A Process holds all the information about one task the CPU needs to run.
class Process:

    # Sets up a new process with its basic information.
    # The waiting time and turnaround time start at zero.
    # They will be calculated later by the FCFS algorithm.
    def __init__(self, process_id, arrival_time, burst_time):
        # TODO: Store process_id, arrival_time, burst_time.
        # Initialize waiting_time and turnaround_time to 0.
        pass


class FCFSAlgorithm:

    # Sets up the FCFS scheduler with an empty queue and an empty list of processes.
    # The queue will hold processes waiting to be run.
    # The list of all processes is kept so we can display results later.
    def __init__(self):
        # TODO: Create self.process_queue as a NodeQueue.
        # Create self.all_processes as an empty list.
        pass

    # Adds a new process to the back of the queue and saves it to our list.
    # This is how a process "arrives" and joins the waiting line.
    def add_process(self, new_process):
        # TODO: Enqueue new_process to the queue.
        # Append new_process to all_processes list.
        pass

    # Runs the FCFS simulation by working through each process in queue order.
    # For each process, it calculates:
    #   - Waiting Time:     how long the process sat idle before the CPU started it.
    #   - Turnaround Time:  total time from arrival to completion (wait + burst).
    # The CPU clock (current_time) keeps track of when the CPU becomes free.
    def run(self):
        # TODO: Initialize current_time to 0.
        # While the queue is not empty, dequeue a process.
        # If current_time < arrival_time, set current_time to arrival_time (CPU idle time).
        # Calculate waiting_time = current_time - arrival_time.
        # Update current_time by adding burst_time.
        # Calculate turnaround_time = current_time - arrival_time.
        pass

    # Calculates and returns the average waiting time across all processes.
    def get_average_waiting_time(self):
        # TODO: Sum all waiting times from all_processes.
        # Divide by the number of processes.
        # Return the result.
        pass

    # Calculates and returns the average turnaround time across all processes.
    def get_average_turnaround_time(self):
        # TODO: Sum all turnaround times from all_processes.
        # Divide by the number of processes.
        # Return the result.
        pass
