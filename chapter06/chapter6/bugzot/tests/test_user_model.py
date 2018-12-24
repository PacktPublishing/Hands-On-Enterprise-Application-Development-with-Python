'''
File: test_user_model.py
Description: Tests for the User database model
'''
import sys
import pytest

sys.path.append('.')

from bugzot.models import User


@pytest.fixture(scope='module')
def create_user():
    user = User(username='joe', password='Hello123', email='joe@gmail.com')
    return user

def test__user_creation(create_user):
    assert create_user.email == 'joe@gmail.com'
    assert create_user.username == 'joe'
