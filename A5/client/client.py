import socket, time

ADDR, BUFFER = ("localhost", 8080), 1024

class TokenRingClient:
    def __init__(self):
        self.s = socket.socket()

    def connect(self):
        self.s.connect(ADDR)
        print("Connected to server")

    def start(self):
        try:
            while True:
                data = self.s.recv(BUFFER).decode()
                if data == "TOKEN":
                    print("Token received. Working..."); 
                    time.sleep(5)
                    print("Done. Passing token."); 
                    self.s.send(b"TOKEN")
                elif data == "CLOSE":
                    print("Server closed connection."); 
                    break
        except KeyboardInterrupt:
            print("Interrupted. Closing..."); 
            self.s.send(b"CLOSE")
        finally:
            self.s.close()

if __name__ == "__main__":
    client = TokenRingClient()
    client.connect()
    client.start()


# Once the server is runned, now run the client -> client.py
# cd client
# python3 client.py

# There will be a loop of tokens being passed



# Concept: Token Ring Algorithm - 
# It's used to ensure only one process accesses a shared resource at a time.
# A token (special message) is passed in a ring among clients.
# Only the client with the token can access the resource.


# client - 
# Connects to the server.
# Waits to receive the token.
# On receiving the token:
# Simulates accessing the resource (e.g., sleep for 5 seconds).
# Then returns the token to the server.
# If it receives a CLOSE message, it shuts down.

