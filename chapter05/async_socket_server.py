#!/usr/bin/python3
import asyncio

class MessageProtocol(asyncio.Protocol):
    """An asyncio protocol implementation to handle the incoming messages."""

    def connection_made(self, transport):
        print("Got a new connection")
        self.transport = transport

    def data_received(self, data):
        print("Data received")
        self.transport.write("Message received".encode('utf-8'))

loop = asyncio.get_event_loop()
server_handler = loop.create_server(MessageProtocol, 'localhost', 7000)
server = loop.run_until_complete(server_handler)
try:
    loop.run_forever()
except KeyboardInterrupt:
    server.close()
    loop.close()
