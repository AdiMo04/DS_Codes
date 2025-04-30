# ring.py

class Ring:
    def __init__(self, num_process):
        self.num_process = num_process
        self.coordinator = num_process  # Initially, highest ID is the coordinator
        self.active_processes = set(range(1, num_process + 1))  # All processes are initially active

    def election(self, process_id):
        if process_id not in self.active_processes:
            print(f"Process {process_id} is not active.")
            return

        highest_id = process_id  # Start with the initiator
        next_process = (process_id % self.num_process) + 1  # Next in ring

        # Pass election message around the ring
        while next_process != process_id:
            if next_process in self.active_processes:
                print(f"Process {process_id} is passing election message to process {next_process}")
                if next_process > highest_id:
                    highest_id = next_process  # Track highest ID seen
            else:
                print(f"Process {next_process} is down and cannot receive the election message.")
            next_process = (next_process % self.num_process) + 1

        # Declare coordinator after full ring traversal
        self.coordinator = highest_id
        print(f"Process {self.coordinator} is the coordinator.")

    def start_election(self, process_id):
        # Begin the election from a specific process
        if process_id in self.active_processes:
            print(f"Process {process_id} starts the election process.")
            self.election(process_id)
        else:
            print(f"Process {process_id} is not active.")

    def bring_up_process(self, process_id):
        # Reactivate a process if it was down
        if process_id in self.active_processes:
            print(f"Process {process_id} is already up.")
        else:
            self.active_processes.add(process_id)
            print(f"Process {process_id} is up.")

    def bring_down_process(self, process_id):
        # Deactivate a process
        if process_id not in self.active_processes:
            print(f"Process {process_id} is already down.")
        else:
            self.active_processes.remove(process_id)
            print(f"Process {process_id} is now down.")

            # If coordinator goes down, start new election
            if self.coordinator == process_id:
                active = list(self.active_processes)
                if active:
                    self.start_election(active[0])
                else:
                    self.coordinator = None  # No active processes

    def print_active_processes(self):
        print("Active processes:", sorted(self.active_processes))

    def print_coordinator(self):
        print(f"Coordinator: Process {self.coordinator}" if self.coordinator else "Coordinator: None")


if __name__ == "__main__":
    try:
        num = int(input("Enter number of processes: "))
        ring = Ring(num)  # Initialize ring algorithm with given processes
    except ValueError:
        print("Invalid input.")
        exit()

    while True:
        print("\n--- Ring Algorithm Menu ---")
        print("1) Start Election")
        print("2) Bring Up Process")
        print("3) Bring Down Process")
        print("4) Print Active Processes")
        print("5) Print Coordinator")
        print("6) Exit")

        try:
            choice = int(input("Enter choice: "))
            if choice == 1:
                pid = int(input("Enter process id: "))
                if 1 <= pid <= num:
                    ring.start_election(pid)
                else:
                    print("Invalid process id.")
            elif choice == 2:
                pid = int(input("Enter process id: "))
                if 1 <= pid <= num:
                    ring.bring_up_process(pid)
                else:
                    print("Invalid process id.")
            elif choice == 3:
                pid = int(input("Enter process id: "))
                if 1 <= pid <= num:
                    ring.bring_down_process(pid)
                else:
                    print("Invalid process id.")
            elif choice == 4:
                ring.print_active_processes()
            elif choice == 5:
                ring.print_coordinator()
            elif choice == 6:
                break
            else:
                print("Invalid menu choice.")
        except ValueError:
            print("Please enter a valid number.")
