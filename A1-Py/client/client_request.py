import sys
import xmlrpc.client

def main():
    search = sys.argv[1] if len(sys.argv) > 1 else "p2p"
    proxy = xmlrpc.client.ServerProxy("http://localhost:1099/")
    result = proxy.query(search)
    print("Found:", result)

if __name__ == "__main__":
    main()



# First you need to run the server -> search_server.py

# After running the server then open new terminal and run the client -> client_request.py
# cd client
# python client_request.py p2p

# Description - 
# You create a function query(search_term) inside the search_interface.py file.
# This function is exposed using XML-RPC so that other machines (clients) can call it over the network.
# The server runs on localhost:8000 (or 1099 earlier).


# In simple words - 
# You created a search function on one machine and used it remotely from another machine using Python’s RPC (Remote Procedure Call). The server shares a method, and the client calls that method as if it was local.
