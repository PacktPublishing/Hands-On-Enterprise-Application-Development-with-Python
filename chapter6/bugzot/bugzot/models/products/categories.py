'''
File: categories.py
Description: The file contains the definition for the categories
             data model which is used for storing the information
             related to the product categories.
'''
from bugzot.application import db


class Category(db.Model):
    """Category model.

    The model is used to store the categories to which the products belong
    so that the products can be easily grouped based on their purpose.
    """

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category_name = db.Column(db.String(100), nullable=False, unique=True, index=True)

    def __repr__(self):
        """Category model representation."""
        return "<Category {}>".format(self.category_name)
