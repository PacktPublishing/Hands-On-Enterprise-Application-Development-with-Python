#!/usr/env/bin python
from multiprocessing import Process, Lock
import urllib.request

def load_url(url, lock):
    url_handle = urllib.request.urlopen(url)
    url_data = url_handle.read()
    # The data returned by read() call is in the bytearray format. We need to
    # decode the data before we can print it.
    url_handle.close()
    lock.acquire()
    with open("combinedhtml.txt", 'a+') as outfile:
        outfile.write(url_data.decode("utf-8"))
    lock.release()

if __name__ == '__main__':
    urls = ['http://www.github.com', 'http://www.packtpub.com']
    lock = Lock()
    process_pool = []
    for url in urls:
        url_loader = Process(target=load_url, args=(url, lock,))
        process_pool.append(url_loader)
    for loader in process_pool:
        loader.start()
    for loader in process_pool:
        loader.join()
    print("Exiting...")
    
