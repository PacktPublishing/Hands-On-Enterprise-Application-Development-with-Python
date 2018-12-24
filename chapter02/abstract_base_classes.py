#!/bin/python3
from abc import ABC, abstractmethod


class AbstractUser(ABC):
  @abstractmethod
  def return_data(self):
    pass

class User(AbstractUser):
  def __init__(self, username):
    self.username = username
    self.user_data = {}
    
  def return_username(self):
    return self.username

  def return_data(self):
    return self.user_data

if __name__ == '__main__':
    usr = User('joe')
    print(usr.return_username())
