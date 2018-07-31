#!/bin/python3

class A:
    def __init__(self):
        print(“Class A”)

class B:
    def __init__(self):
        print(“Class B”)

class C(A,B):
    def __init__(self):
        print(“Class C”)
