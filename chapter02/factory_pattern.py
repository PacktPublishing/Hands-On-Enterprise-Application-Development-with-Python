#!/bin/python3
from abc import ABC, abstractmethod

class HTMLFormEntity(ABC):
  def __init__(self, id, name):
    self.id = id
    self.name = name
  @abstractmethod
  def render(self):
    pass

class Button(HTMLFormEntity):
  def __init__(self, id, name):
    super().__init__(id, name)
    self.type = "button"
  def render(self):
    html = "<input id={idx} name={name} type={itype} />"
    return html.format(idx=self.id, name=self.name, itype=self.type)

class Text(HTMLFormEntity):
  def __init__(self, id, name):
    super().__init__(id, name)
    self.type = "text"
  def render(self):
    html = "<input id={idx} name={name} type={itype} />"
    return html.format(idx=self.id, name=self.name, itype=self.type)

class HTMLForm(HTMLFormEntity):
  __elements = {
    "button": Button,
    "text": Text
  }
  def __init__(self, id, name, action, method):
    super().__init__(id, name)
    self.action = action
    self.method = method
    self.elements = []
  def add_entity(self, entity_type, id, name):
    if entity_type in self.__elements.keys():
      self.elements.append(self.__elements[entity_type](id, name)) 
  def render(self):
    # render method body
    pass

if __name__ == '__main__':
    form = HTMLForm("testform", "TestForm", "post.py", "POST")
    form.add_entity("button", "button1", "submit")
    form.add_entity("text", "username", "username")
