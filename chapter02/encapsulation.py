#!/bin/python3
class PyOOP:
    __name = None

    def __init__(self, name):
        self.__name = name

    def get_name():
        return self.__name

pobj = PyOOP('Joe')
print(pobj.__name)
