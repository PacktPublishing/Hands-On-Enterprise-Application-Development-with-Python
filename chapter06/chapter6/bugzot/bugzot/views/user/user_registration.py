'''
File: user_registration.py
Description: The file contains the definition for the user registration
             view allowing new users to register to the BugZot.
'''
from bugzot.application import app, brcypt, db
from bugzot.models import User, Role
from flask.views import MethodView
from datetime import datetime
from flask import render_template, session


class UserRegistrationView(MethodView):
    """User registration view to allow new user registration.

    The user registration view allows for the registering of the new users
    to the bugzot bug tracking system. The view allows the application
    to render the user registration page along with the handling of the
    submitted data.
    """

    __keys = ['username', 'password', 'confirm_password', 'email']

    def get(self):
        """HTTP GET handler."""

        username = session.get('username', None)

        # Check if there is an active user session
        if username is None:
            return render_template('user/registration.html')
        
        return render_template('index/index.html', logged_in=True, username=username)

    def post(self):
        """HTTP POST handler."""

        form_data = {}
        
        # Iterate over the form to validate the existence of all the
        # required keys and store their data
        for form_key in self.__keys:
            if not request.form.has_key(form_key):
                return "All fields are required"
            else:
                form_data[form_key] = request.form.get(form_key)

        # Validate if the passwords match
        if not self.__validate_passwords(form_data['password'], form_data['confirm_password']):
            return "Passwords do not match"

        # Generate a new model
        user = self.__generate_model(form_data)

        # Save the model to the database
        db.session.add(user)
        db.session.commit()

        # Return a success page
        return render_template("user/registration_success.html")


    def __generate_model(self, form_data):
        """Generate the user data model.

        Returns:
            db.Model
        """

        username = form_data['username']
        email = form_data['email']
        password = bcrypt.generate_password_hash(form_data['password']).decode('utf-8')

        # Determine the user role and id
        role = Role.query.filter(role_name='user').first()
        joining_date = datetime.now()
        last_login = datetime.now()

        user = User(username=username, email=email, password=password, role=role, joining_date=joining_date, last_login=last_login)
        return user


    def __validate_passwords(self, password, confirm_password):
        """Validate if the passwords match or not.

        Returns:
            Boolean
        """
        if password != confirm_password:
            return False
        return True

