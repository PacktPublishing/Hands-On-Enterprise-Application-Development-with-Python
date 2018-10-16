'''
File: versions.py
Description: The file contains the defintion for the Version
             model which is used to track the version information
             related to individual products.
'''
from bugzot.application import db
from .products import Product


class Version(db.Model):
    """Version information model.

    The model is used to store the information of the product versions
    on a per product basis.
    """

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    version = db.Column(db.String(20), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey(Product.id))

    def __repr__(self):
        """Version model representation."""
        return "<Version {}>".format(self.version)
