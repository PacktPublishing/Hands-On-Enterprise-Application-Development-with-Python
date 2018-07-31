#!/bin/python3

class LoggerMeta(type):
  def __init__(cls, name, base, dct):
    for k in dct.keys():
      if k.startswith(‘HANDLER_’):
        if not callable(dct[k]):
          raise AttributeError(“{} is not callable”.format(k))
    super().__init__(name, base, dct)


def error_handler():
  print(“error”)
def warning_handler():
  print(“warning”)


class Log(metaclass=LoggerMeta):
  HANDLER_ERROR = error_handler
  HANDLER_WARN = warning_handler
  HANDLER_INFO = ‘info_handler’

  def __init__(self):
    print(“Logger class”)
