#!/bin/python3
str1 = 'I am a unicode string'
print("Type of str1 is " + str(type(str1)))
str2 = b"And I can't be concatenated to a byte string"
print("Type of str2 is " + str(type(str2)))
print("Trying to concatenate str1 and str2")
str3 = str1 + str2
