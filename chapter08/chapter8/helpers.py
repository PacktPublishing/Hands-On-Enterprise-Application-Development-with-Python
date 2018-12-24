'''
File: helpers.py
Description: Helper functions to handle the user password management
Author: Saurabh Badhwar
'''
import hashlib
import secrets

def strip_password(password):
    """Strip the trailing and leading whitespace.
    
    Returns:
        String
    """
    return password.strip()

def generate_salt(num_bytes=8):
    """Generate a new salt

    Keyword arguments:
    num_bytes -- Number of bytes of random salt to generate

    Returns:
        Bytes
    """

    return secrets.token_bytes(num_bytes)

def encrypt_password(password, salt):
    """Encrypt a provided password and return a hash.

    Keyword arguments:
    password -- The plaintext password to be encrypted
    salt -- The salt to be used for padding

    Returns:
        String
    """

    passwd_hash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 10000).hex()
    return passwd_hash
