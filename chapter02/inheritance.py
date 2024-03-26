#!/bin/python3

class Request:
  def __init__(self, title, description, is_private=False):
    self.title = title
    self.description = description
    self.is_private = is_private

  def get_request(self):
    request_data = {
      'title': self.title,
      'description': self.description,
      'is_private': self.is_private
    }

class Bug(Request):
  def __init__(self, title, description, affected_release, severity, is_private):
    self.affected_release = affected_release
    self.severity = severity
    super().__init__(title, description, is_private)

  def get_bug(self):
    bug_data = {
      'title': self.title,
      'description': self.description,
      'severity': self.severity,
      'affected_release': self.affected_release,
      'is_private': self.is_private
    }
    return bug_data
