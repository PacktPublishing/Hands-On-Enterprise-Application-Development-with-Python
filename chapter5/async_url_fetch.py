#!/usr/bin/python3
import asyncio
import requests

async def fetch_url(url):
   response = requests.get(url)
   return response.text

async def get_url(url):
    return await fetch_url(url)

def process_results(future):
    print("Got results")
    print(future.result())

loop = asyncio.get_event_loop()
task1 = loop.create_task(get_url('http://www.google.com'))
task2 = loop.create_task(get_url('http://www.microsoft.com'))
task1.add_done_callback(process_results)
task2.add_done_callback(process_results)
loop.run_forever()

