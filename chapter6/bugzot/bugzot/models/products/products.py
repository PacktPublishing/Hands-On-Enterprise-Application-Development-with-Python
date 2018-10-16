'''
File: products.py
Description: The file contains the definition for the products
             that are supported for bug filing inside the bug tracker
'''
from bugzot.application import db
from .categories import Category


class Product(db.Model):
    """Product defintion model.

    The model is used to store the information related to the products
    for which the users can file a bug.
    """

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_name = db.Column(db.String(100), nullable=False, unique=True, index=True)
    category_id = db.Column(db.Integer, db.ForeignKey(Category.id))
    category = db.relationship("Category", lazy=True)

    def __repr__(self):
        """Product model representation."""
        return "<Product {}>".format(self.product_name)
