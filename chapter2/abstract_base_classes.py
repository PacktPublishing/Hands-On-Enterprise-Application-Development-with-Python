#!/bin/python3
from abc import ABC, abstractmethod


def AbstractUser(ABC):
  @abstractmethod
  def return_data(self):
    pass

def User(AbstractUser):
  def __init__(self, username):
    self.username = username
    self.user_data = {}
  def return_username(self):
    return self.username
  def return_data(self)
    return self.user_data
