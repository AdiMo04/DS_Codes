import socket, threading

TOKEN, PORT, BUFFER = "TOKEN", 8080, 1024

class TokenRingServer:
    def __init__(self):
        self.s = socket.socket(); 
        self.s.bind(("localhost", PORT)); 
        self.s.listen()
        self.clients, self.threads, self.running = [], [], True

    def start(self):
        print("Server started. Listening...")
        try:
            while self.running:
                c, _ = self.s.accept()
                print(f"Client connected: {c.getpeername()}")
                self.clients.append(c)
                if len(self.clients) == 1: 
                    c.send(TOKEN.encode())
                t = threading.Thread(target=self.handle, args=(c,))
                t.start(); 
                self.threads.append(t)
        except KeyboardInterrupt:
            self.stop()

    def handle(self, c):
        while self.running:
            try:
                data = c.recv(BUFFER).decode()
                if data == "CLOSE":
                    print(f"Client left: {c.getpeername()}")
                    self.clients.remove(c); 
                    c.close(); 
                    break
                if data == TOKEN and self.clients:
                    nxt = self.clients[(self.clients.index(c) + 1) % len(self.clients)]
                    print("Passing token")
                    nxt.send(TOKEN.encode())
            except: break

    def stop(self):
        self.running = False
        print("Shutting down...")
        for c in self.clients:
            try: 
                c.send("CLOSE".encode()); 
                c.close()
            except: pass
        for t in self.threads: 
            t.join()
        self.s.close()

if __name__ == "__main__":
    TokenRingServer().start()



# Simply run the server first -> server.py
# cd server
# python3 server.py

# Now go and run the client 


# server - 
# Accepts connections from multiple clients.
# Maintains a list of connected clients (like a ring).
# Passes the token to one client at a time.
# When a client is done, the token goes to the next client in the list.
# If a client disconnects, it's removed from the ring.


#  How it works - 
# Server starts and waits for clients.
# Clients connect one by one.
# First client gets the token.
# Each client, after using the token, passes it back to server.
# Server forwards it to the next client, like a circle (ring).
# You can simulate multiple rounds of mutual exclusion.

