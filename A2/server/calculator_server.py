import Pyro5.api

@Pyro5.api.expose  # This decorator exposes the class methods to Pyro
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero"
        return a / b

def main():
    # Initialize the Pyro daemon
    daemon = Pyro5.api.Daemon()

    # Register the Calculator class with the daemon
    calculator = Calculator()
    uri = daemon.register(calculator)

    # Print the URI for clients to use
    print(f"Ready. Object URI = {uri}")

    # Start the daemon to listen for client requests
    daemon.requestLoop()

if __name__ == "__main__":
    main()


# First you need to run the server
# cd server
# python3 calculator_server.py

# Once the server is runned, copy the object URI from the server

# Now, you can run the client



# Description - 
# This assignment involves creating a Client-Server application using Pyro5, a Python library for Remote Method Invocation (RMI). Here's a summary of the key steps and concepts:
# A calculator server is created that exposes methods for performing basic arithmetic operations: add, subtract, multiply, and divide.
# The server is registered with Pyro5, allowing remote clients to call these methods over the network.



# Summary for Explanation - 
# The server exposes methods to perform arithmetic operations.
# The client connects to the server using Pyro5 and allows the user to interactively choose operations and input numbers.
# The client sends the chosen operation and numbers to the server, which computes the result and sends it back.
# The result is displayed on the client, and the process continues until the user exits.




