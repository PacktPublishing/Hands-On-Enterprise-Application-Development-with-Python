'''
File: test_index_route.py
Description: Test the index application route
'''
import os
import pytest
import sys
import tempfile

sys.path.append('.')

import bugzot

@pytest.fixture(scope='module')
def client():
    db_fd, bugzot.app.config['DATABASE'] = tempfile.mkstemp()
    bugzot.app.config['TESTING'] = True
    client = bugzot.app.test_client()

    with bugzot.app.app_context():
        bugzot.db.create_all()

    yield client
    
    os.close(db_fd)
    os.unlink(bugzot.app.config['DATABASE'])

def test_index_endpoint(client):

    res = client.get("/")
    dir(res)
    assert res.status_code == 200

