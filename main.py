# This is the main file that runs the FCFS scheduling algorithm simulation.
# It collects process information from the user, runs the FCFS algorithm,
# and then displays the results in a formatted table.

from fcfs_algorithm import Process, FCFSAlgorithm
from node_queue import NodeQueue
from queue_blueprint import QueueIsEmptyError


# Welcome the user and wait for them to press Enter before starting.
# This mirrors the "Press OK" prompt from the original Java version.
print("===============================================")
print("   FCFS CPU Scheduling Algorithm Simulation   ")
print("===============================================")
input("Press Enter to start the simulation...")
print("")

# Ask the user how many processes they want to simulate.
number_of_processes = int(input("Enter the number of processes: "))
print("")

# Create the FCFS scheduler.
scheduler = FCFSAlgorithm()

# Ask the user for arrival time and burst time for each process.
# Then create a Process object and add it to the scheduler.
process_number = 1
while process_number <= number_of_processes:
    arrival_time = int(input("Enter arrival time for process P" + str(process_number) + ": "))
    burst_time = int(input("Enter burst time for process P" + str(process_number) + ": "))
    new_process = Process("P" + str(process_number), arrival_time, burst_time)
    scheduler.add_process(new_process)
    process_number = process_number + 1

# Run the FCFS algorithm to calculate waiting and turnaround times.
scheduler.run()

# Display the results in a formatted table.
print("")
print("===============================================")
print("               SIMULATION RESULTS             ")
print("===============================================")
print("")

# Print the table header row.
print(f"{'Process':<10} {'Arrival':<10} {'Waiting':<10} {'Turnaround'}")
print("-" * 45)

# Print one row per process.
for process in scheduler.all_processes:
    print(
        f"{process.process_id:<10} "
        f"{process.arrival_time:<10} "
        f"{process.waiting_time:<10} "
        f"{process.turnaround_time}"
    )

# Display the average results below the table.
print("")
user_input = input("Press any button to continue or 0 to exit: ")
if user_input == "0":
    exit()
print("")
print("===============================================")
print("                   AVERAGES                   ")
print("===============================================")
average_waiting = scheduler.get_average_waiting_time()
average_turnaround = scheduler.get_average_turnaround_time()
print("Average Waiting Time:     " + str(round(average_waiting, 2)))
print("Average Turnaround Time:  " + str(round(average_turnaround, 2)))
print("===============================================")
