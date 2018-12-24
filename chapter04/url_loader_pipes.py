#!/usr/env/bin python
from multiprocessing import Process, Pipe
import urllib.request

def load_url(url, pipe):
    url_handle = urllib.request.urlopen(url)
    url_data = url_handle.read()
    # The data returned by read() call is in the bytearray format. We need to
    # decode the data before we can print it.
    html_data = url_data.decode('utf-8')
    url_handle.close()
    pipe.send(html_data)
    

if __name__ == '__main__':
    url = 'http://www.w3c.org'
    parent_pipe, child_pipe = Pipe()
    loader_process = Process(target=load_url, args=(url, child_pipe))
    print("Spawning a new process to load the url")
    loader_process.start()
    print("Waiting for the spawned process to exit")
    html_data = parent_pipe.recv()
    print(html_data)
    loader_process.join()
    print("Exiting...")

