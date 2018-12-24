#!/usr/bin/python3
import socket
import threading


#Let's first create a TCP type Server for handling clients
class Server(object):
    """A simple TCP Server."""

    def __init__(self, hostname, port):
        """Server initializer

        Keyword arguments:
        hostname -- The hostname to use for the server
        port -- The port on which the server should bind
        """

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.hostname = hostname
        self.port = port
        self.bind_connection()
        self.listen()

    def bind_connection(self):
        """Bind the server to the host."""

        self.server.bind((self.hostname, self.port))

    def listen(self):
        """Start listening for the incoming connections."""

        self.server.listen(10) # Queue a maximum of 10 clients
        #Enter the listening loop
        while True:
            client, client_addr = self.server.accept()
            print("Received a connection from %s" % str(client_addr))
            client_thread = threading.Thread(target=self.handle_client, args=(client,))
            client_thread.daemon = True
            client_thread.start()

    def handle_client(self, client):
        """Handle incoming client connection.

        Keyword arguments:
        client -- The client connection socket
        """

        print("Accepted a client connection")
        while True:
            buff = client.recv(1024).decode()
            if not buff:
                break
            print(buff)
        print("Client closed the connection")
        client.close() # We are done now, let's close the connection

if __name__ == '__main__':
    server = Server('localhost', 7001)
