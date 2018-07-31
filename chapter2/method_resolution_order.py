#!/bin/python3

class A:
  def __init__(self):
    print(“Class A”)
    super().__init__()

class B:
  def __init__(self):
    print(“Class B”)
    super().__init__()

class C(A,B):
  def __init__(self):
    print(“Class C”)
    super().__init__()
Cobj = C()
