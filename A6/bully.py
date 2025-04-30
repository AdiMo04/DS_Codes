# bully.py

# bully.py

class Bully:
    def __init__(self, num_process):
        # Initialize process states as alive (True)
        self.num_process = num_process
        self.state = [True for _ in range(num_process)]
        self.leader = num_process  # Highest ID process is the initial coordinator

    def election(self, process_id):
        print(f"Process {process_id} is sending election messages to higher processes")
        cod = process_id
        # Send election message to all higher processes
        for i in range(process_id + 1, self.num_process + 1):
            if self.state[i - 1]:  # Check if process is alive
                print(f"Process {process_id} is sending election message to process {i}")
                cod = i  # Update candidate coordinator

        print(f"Process {cod} is sending coordinator message to all")
        self.leader = cod  # Declare coordinator
        print(f"Process {self.leader} is now coordinator.")

    def up(self, process_id):
        # Bring up a process and initiate election
        if self.state[process_id - 1]:
            print(f"Process {process_id} is already up")
        else:
            self.state[process_id - 1] = True
            print(f"Process {process_id} is up")
            self.election(process_id)

    def down(self, process_id):
        # Bring down a process
        if not self.state[process_id - 1]:
            print(f"Process {process_id} is already down.")
        else:
            self.state[process_id - 1] = False
            print(f"Process {process_id} is now down")

            # If leader goes down, elect a new one
            if self.leader == process_id:
                active = [i + 1 for i, val in enumerate(self.state) if val]
                if active:
                    import random
                    index = random.randint(0, len(active) - 1)
                    self.election(active[index])
                else:
                    print("No active processes to elect coordinator.")

    def message(self, process_id):
        # Simulate message sending from a process
        if self.state[process_id - 1]:
            if self.state[self.leader - 1]:
                print("OK")  # Coordinator is alive
            else:
                self.election(process_id)  # Re-elect if coordinator is down
        else:
            print(f"Process {process_id} is down.")


if __name__ == "__main__":
    try:
        num = int(input("Enter number of processes: "))
        bully = Bully(num)
        print(f"{num} Active processes initialized.")
        print(f"Processes up: {' '.join([f'p{i+1}' for i in range(num)])}")
        print(f"Process {bully.leader} is the coordinator")
    except ValueError:
        print("Invalid input. Please enter an integer.")
        exit()

    while True:
        print("\n--- Bully Algorithm Menu ---")
        print("1) Up a process")
        print("2) Down a Process")
        print("3) Send a Message")
        print("4) Exit")

        try:
            choice = int(input("Enter choice: "))
            if choice == 1:
                pid = int(input("Enter process id: "))
                if 1 <= pid <= num:
                    bully.up(pid)
                else:
                    print("Invalid process id.")
            elif choice == 2:
                pid = int(input("Enter process id: "))
                if 1 <= pid <= num:
                    bully.down(pid)
                else:
                    print("Invalid process id.")
            elif choice == 3:
                pid = int(input("Enter process id: "))
                if 1 <= pid <= num:
                    bully.message(pid)
                else:
                    print("Invalid process id.")
            elif choice == 4:
                break
            else:
                print("Invalid menu choice.")
        except ValueError:
            print("Please enter a valid number.")






#Run Bully Algorithm- python bully.py

# Run Ring Algorithm - python ring.py

# start by down a process option, and select the highest numbered process.
