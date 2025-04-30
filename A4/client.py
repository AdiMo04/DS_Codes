# client.py
import socket     # For network communication
import time       # For real-time clock reference
import json       # For encoding and decoding messages
import random     # To simulate out-of-sync clock

SERVER_IP = "127.0.0.1"  # Server IP address
PORT = 5000              # Server port


def get_local_time():
    # Simulates a skewed local time using random offset
    return random.randint(int(time.time() - 1e5), int(time.time() + 1e5))


def main():
    # Create TCP socket and connect to server
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_IP, PORT))
    print(f"Connected to {SERVER_IP}:{PORT}")

    client_local_time = get_local_time()  # Get this client's local time
    time_adjusted = False  # Flag to control loop

    while not time_adjusted:
        server_res = json.loads(client_socket.recv(1024).decode())  # Receive message from server

        if server_res["operation"] == "time_req":
            # Server requested time, send current local time
            print(f"Local time: {client_local_time}")
            client_socket.send(json.dumps({"client_time": client_local_time}).encode())

        if server_res["operation"] == "time_adj":
            # Server sent adjustment offset
            print(f"Time adjustment: {server_res['adjusted_time']}")
            client_local_time += float(server_res["adjusted_time"])  # Apply adjustment
            print(f"Adjusted time: {client_local_time}")
            time_adjusted = True

    client_socket.close()  # Close socket after adjustment


if __name__ == "__main__":
    main()




# for each new client open a new terminal and run : pyhton client.py
# before this type y in server terminal