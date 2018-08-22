#!/usr/env/bin python
import threading

class EmailQueue(threading.Thread):

    def __init__(self, email_queue, max_items, condition_var):
        threading.Thread.__init__(self)
        self.email_queue = email_queue
        self.max_items = max_items
        self.condition_var = condition_var
        self.email_recipients = []

    def add_recipient(self, email):
        self.email_recipients.append(email)

    def run(self):
        while True:
            self.condition_var.acquire()
            if len(self.email_queue) == self.max_items:
                print("E-mail queue is full. Entering wait state...")
                self.condition_var.wait()
                print("Received consume signal. Populating queue...")
            while len(self.email_queue) < self.max_items:
                if len(self.email_recipients) == 0:
                    break
                email = self.email_recipients.pop()
                self.email_queue.append(email)
                self.condition_var.notify()
            self.condition_var.release()

class EmailSender(threading.Thread):

    def __init__(self, email_queue, condition_var):
        threading.Thread.__init__(self)
        self.email_queue = email_queue
        self.condition_var = condition_var

    def run(self):
        while True:
            self.condition_var.acquire()
            if len(self.email_queue) == 0:
                print("E-mail queue is empty. Entering wait state...")
                self.condition_var.wait()
                print("E-mail queue populated. Resuming operations...")
            while len(self.email_queue) is not 0:
                email = self.email_queue.pop()
                print("Sending email to {}".format(email))
            self.condition_var.notify()
            self.condition_var.release()

queue = []
MAX_QUEUE_SIZE = 100
condition_var = threading.Condition()

email_queue = EmailQueue(queue, MAX_QUEUE_SIZE, condition_var)
email_sender = EmailSender(queue, condition_var)
email_queue.start()
email_sender.start()
email_queue.add_recipient("joe@example.com")

