'''
File: components.py
Description: The file contains the defintion for the components model
             which is used to store the information related to the 
             different components against which the bugs can be filed
             for a particular product.
'''
from bugzot.application import db
from bugzot.models.users import User
from .products import Product


class Component(db.Model):
    """Components model for tracking product components.

    The model is used to keep a record of the components for which
    the bugs can be filed. This provides a more targeted approach to
    classifying the busg inside the system.
    """

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    component_name = db.Column(db.String(100), unique=True, nullable=False, index=True)
    product_id = db.Column(db.Integer, db.ForeignKey(Product.id))
    product = db.relationship("Product", lazy=True)
    component_owner = db.Column(db.Integer, db.ForeignKey(User.id))

    def __repr__(self):
        """Component model representation."""
        return "<Component {}>".format(self.component_name)
