import Pyro5.api

def main():
    # Ask for the server object URI
    uri = input("Enter the object URI from the server: ")
    
    # Connect to the Pyro5 server
    calculator = Pyro5.api.Proxy(uri)
    
    while True:
        print("\n--- Menu ---")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        
        choice = input("Choose an operation (1-5): ")
        
        if choice == '5':
            print("Exiting...")
            break
        
        # Take input for numbers
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input, please enter numbers.")
            continue
        
        # Perform the chosen operation
        if choice == '1':
            result = calculator.add(num1, num2)
            print(f"{num1} + {num2} = {result}")
        elif choice == '2':
            result = calculator.subtract(num1, num2)
            print(f"{num1} - {num2} = {result}")
        elif choice == '3':
            result = calculator.multiply(num1, num2)
            print(f"{num1} * {num2} = {result}")
        elif choice == '4':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                result = calculator.divide(num1, num2)
                print(f"{num1} / {num2} = {result}")
        else:
            print("Invalid choice. Please select a valid operation.")
    
if __name__ == "__main__":
    main()




# First you need to run the server

# Once the server is runned, copy the object URI from the server

# Then you can run the client -> calculator_client.py
# cd client
# python3 calculator_client.py

# Description - 
# The client connects to the server using a unique object URI (Universal Resource Identifier), which the server provides.
# The client presents a menu interface to the user, offering options for performing arithmetic operations.
# The client allows the user to input two numbers and choose an operation.
# The client sends the operation request to the server, which performs the computation and sends the result back to the client.
# The client displays the result to the user.


# Pyro5 - 
# Pyro5 is used to enable communication between the client and the server. It allows remote invocation of methods (i.e., calling methods on the server from the client as if they were local).
# The client can perform any of the operations (add, subtract, multiply, divide) on the server, and the results are sent back to the client.