# server.py
import socket      # For network communication
import time        # For time-related operations
import random      # To simulate clock skew
import json        # To encode/decode data for communication

SERVER_IP = "127.0.0.1"  # Localhost
PORT = 5000              # Port to bind the server socket


def get_local_time():
    # Simulates an out-of-sync local time by generating a random time offset
    return random.randint(int(time.time() - 1e5), int(time.time() + 1e5))


def main():
    # Create and bind a TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((SERVER_IP, PORT))
    server_socket.listen(1)  # Allow 1 unaccepted connection in the queue

    server_local_time = get_local_time()  # Get server's current (skewed) time

    print(f"Time server listening on {SERVER_IP}:{PORT}")
    print(f"Server time: {server_local_time}")

    is_client_enough = False
    clients = []  # List to store connected client sockets

    # Accept clients until user decides to stop
    while not is_client_enough:
        client_socket, client_address = server_socket.accept()  # Accept client
        print(f"Connection established with {client_address}")
        clients.append(client_socket)

        # Ask user if more clients are to be connected
        option = input("Do you want to add more clients? (y/n) ")
        if option.lower() == "n":
            is_client_enough = True
        else:
            print("Waiting for more clients...\n")

    client_local_times = []

    # Request time from each client
    for client_socket in clients:
        time_req_body = json.dumps({"operation": "time_req"})  # Request message
        client_socket.send(time_req_body.encode())             # Send request

        # Receive client time
        client_local_time_response = json.loads(client_socket.recv(1024).decode())
        client_local_times.append(float(client_local_time_response["client_time"]))

    # Compute average offset including server
    average_offset = sum(client_local_times) / len(client_local_times)
    adjusted_time_offset = (server_local_time + average_offset) / 2

    # Send time adjustment to each client
    for i, client_socket in enumerate(clients):
        print(f"Client {client_socket.getpeername()} LocalTime : {client_local_times[i]}")
        adjusted_time = json.dumps({
            "adjusted_time": client_local_times[i] - adjusted_time_offset,  # Offset to apply
            "operation": "time_adj"
        })

        client_socket.send(str(adjusted_time).encode())  # Send adjustment
        print(f"Adjusted time sent to {client_socket.getpeername()}")

    server_socket.close()  # Shutdown server


if __name__ == "__main__":
    main()




#1: To run: pyhton server.py
#2: then open client file and open a terminal in that, type pyhton client.py
#3: go back to server terminal and type y for adding new client.
#4: go to client and open your 2nd terminal and again repeat from step 2.
#5: like this multpile client terminal will be open 
# finally type n for not adding any more clients in server terminal.
#process ends