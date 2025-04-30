import sys
import os

# Add the parent directory (root of the project) to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from remotes import search_interface
from xmlrpc.server import SimpleXMLRPCServer


# from xmlrpc.server import SimpleXMLRPCServer
# from remotes import search_interface

def main():
    server = SimpleXMLRPCServer(("localhost", 1099), allow_none=True)
    print("Search Server ready...")
    server.register_function(search_interface.query, "query")
    server.serve_forever()

if __name__ == "__main__":
    main()



# First you need to run the server -> search_sever.py 
# cd server
# python search_server.py

# Now run the client -> client_request.py

# Description - 
# The client connects to the server using xmlrpc.client.ServerProxy("http://localhost:8000/").
# It sends a search term (like "p2p") to the query() function on the server.
# The server processes it and returns the result ("Found 1 result" or "No results found").