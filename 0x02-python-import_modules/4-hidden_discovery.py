#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    arr = dir()
    for i in range(0, len(arr)):
        if arr[i][:2] != "_":
            print("{:s}".format(arr[i]))
