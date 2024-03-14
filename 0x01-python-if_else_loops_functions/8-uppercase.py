#!/usr/bin/python3
def uppercase(str):
    for i in str:
        temp = i
        if ord(i) >= 97 and ord(i) <= 122:
            temp = chr(ord(i) - 32)
        print("{}".format(temp), end='')
    print()
