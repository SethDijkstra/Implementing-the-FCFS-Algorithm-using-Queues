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
        # nice string for debugging
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
        current_time = 0  # keeps track of time

        # We will iterate over the queue using __iter__
        for process in self.process_queue:
            # if the CPU is idle waiting for the next process to arrive
            if current_time < process.arrival_time:
                current_time = process.arrival_time

            # waiting time = time CPU waited before picking up this process
            process.waiting_time = current_time - process.arrival_time

            # run the process
            current_time += process.burst_time

            # turnaround = total time from arrival to finish
            process.turnaround_time = current_time - process.arrival_time

        # After simulation, clear the queue
        self.process_queue.clear()

    # returns average waiting time
    def get_average_waiting_time(self):
        total = sum(p.waiting_time for p in self.all_processes)
        return total / len(self.all_processes) if self.all_processes else 0

    # returns average turnaround time
    def get_average_turnaround_time(self):
        total = sum(p.turnaround_time for p in self.all_processes)
        return total / len(self.all_processes) if self.all_processes else 0

    # optional: print queue without modifying it (demonstrates iteration)
    def print_queue(self):
        if self.process_queue.is_empty():
            print("Queue is empty")
        else:
            print("Current queue:")
            for process in self.process_queue:  # <-- uses __iter__()
                print(f"{process.process_id} (Arrival: {process.arrival_time}, Burst: {process.burst_time})")
