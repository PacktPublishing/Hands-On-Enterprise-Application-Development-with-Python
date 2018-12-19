#!/bin/python3
import json

class JSONMixin:
  def return_json(self, data):
    try:
      json_data = json.dumps(data)
    except TypeError:
      print("Unable to parse the data into JSON")
    return json_data
