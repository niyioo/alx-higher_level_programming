#!/usr/bin/python3
def uppercase(str):
    result = ""
    for char in str:
        if 'a' <= char <= 'z':
            char = chr(ord(char) - 32)
        result += char
    print("{}".format(result))

