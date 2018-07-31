#!/bin/python3
class MessageHandler:
  __message_type = [‘Error’, ‘Information’, ‘Warning’, ‘Debug’]
  
  def __init__(self, date_format):
    self.date_format = date_format
  
  def new_message(message, message_code, message_type=’Information’):
    if message_type not in self.__message_type:
      raise Exception(“Unable to handle the message type”)
    msg = “[{}] {}: {}”.format(message_type, message_code, message)
    return msg

class WatchDog:

  def __init__(self, message_handler, debug=False):
    self.message_handler = message_handler
    self.debug = debug

  def new_message(message, message_code, message_type):
    try:
      msg = self.message_handler.new_message(message, message_code, message_type)
    except Exception:
      print(“Unable to handle the message type”)
    return msg

message_handler = MessageHandler(‘%Y-%m-%d’)
watchdog = WatchDog(message_handler)
