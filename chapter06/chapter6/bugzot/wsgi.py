'''
File: wsgi.py
Description: WSGI interface file to run the application through WSGI interface
'''
from bugzot import app

if __name__ == '__main__':
    app.run()
