'''
File: index.py
Description: The file provides the definition for the index view
             which is used to render the homepage of Bugzot.
'''
from bugzot.application import app
from flask.views import MethodView
from flask import render_template, session


class IndexView(MethodView):
    """Index view provides the method of rendering the homepage.

    The view is responsible for rendering of the index page of the bugzot
    when a HTTP GET request is made to the server.
    """

    def get(self):
        """HTTP GET request handler."""

        username = session.get('username', None)

        if not username:
            return render_template("index/index.html", logged_in=False)
        else:
            return render_template("index/index.html", logged_in=True, username=username)
