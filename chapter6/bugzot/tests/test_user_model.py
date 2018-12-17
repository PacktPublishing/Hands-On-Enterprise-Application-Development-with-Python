'''
File: test_user_model.py
Description: Tests for the User database model
'''
import sys
import pytest

sys.path.append('.')

from bugzot.models import User


@pytest.fixture(scope='module')
def new_user():
    user = User(username='joe', password='Hello123', email='joe@gmail.com')
    return user

def test_new_user(new_user):
    assert new_user.email == 'joe@gmail.com'
