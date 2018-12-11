'''
File: models.py
Description: The models for the todo service.
'''
from todo_service.todo_service import db
import datetime

class List(db.Model):
    """The list database model.

    The list database model is used to create a new todo list
    based on the input provided by the user.
    """

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    list_name = db.Column(db.String(25), nullable=False)
    db.UniqueConstraint('user_id', 'list_name', name='list_name_uiq')

    def __repr__(self):
        """Provide a representation of model."""
        return "<List {}>".format(self.list_name)

class Item(db.Model):
    """The item database model.

    The model is used to store the information about the items
    in a particular list maintained by the user.
    """

    id = db.Column(db.Integer, primary_key=True)
    list_id = db.Column(db.Integer, db.ForeignKey(List.id))
    item_name = db.Column(db.String(50), nullable=False)
    db.UniqueConstraint('list_id', 'item_name', name='item_list_uiq')

    def __repr__(self):
        """Provide a representation of model."""
        return "<Item {}>".format(self.item_name)
