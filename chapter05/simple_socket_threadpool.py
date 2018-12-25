#!/usr/bin/python3
from concurrent.futures import ThreadPoolExecutor
import socket
import threading


#Let's first create a TCP type Server for handling clients
class Server(object):
    """A simple TCP Server."""

    def __init__(self, hostname, port, pool_size):
        """Server initializer

        Keyword arguments:
        hostname -- The hostname to use for the server
        port -- The port on which the server should bind
        """

        # Setup thread pool size
        self.executor_pool = ThreadPoolExecutor(max_workers=pool_size)

        # Setup the TCP socket server
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
        print("Socket server has started, press Ctrl+C to exit...")
        #Enter the listening loop
        while True:
            client, client_addr = self.server.accept()
            print("Received a connection from %s" % str(client_addr))
            self.executor_pool.submit(self.handle_client, client)

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
    server = Server('localhost', 7005, 20)
