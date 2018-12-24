#!/usr/env/bin python
from multiprocessing import Process
import urllib.request

def load_url(url):
    url_handle = urllib.request.urlopen(url)
    url_data = url_handle.read()
    # The data returned by read() call is in the bytearray format. We need to
    # decode the data before we can print it.
    html_data = url_data.decode('utf-8')
    url_handle.close()
    print(html_data)

if __name__ == '__main__':
    url = 'http://www.w3c.org'
    loader_process = Process(target=load_url, args=(url,))
    print("Spawning a new process to load the url")
    loader_process.start()
    print("Waiting for the spawned process to exit")
    loader_process.join()
    print("Exiting...")

