'''
File: helpers_test.py
Description: Tests for helpers
Author: Saurabh Badhwar
'''
from helpers import strip_password, encrypt_password
import unittest

class TestPasswordHelpers(unittest.TestCase):
    """Unit tests for Password helpers."""

    def test_strip_password(self):
        """Test the strip password function."""

        self.assertEqual(strip_password(' saurabh '), 'saurabh')

    def test_encrypt_password(self):
        """Test the encrypt password function."""

        salt = b'\xf6\xb6(\xa1\xe8\x99r\xe5\xf6\xa5Q\xa9\xd5\xc1\xad\x08'
        encrypted_password = '2ba31a39ccd2fb7225d6b1ee564a6380713aa94625e275e59900ebb5e7b844f9'

        self.assertEqual(encrypt_password('saurabh', salt), encrypted_password)

if __name__ == '__main__':
    unittest.main()
