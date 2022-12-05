#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    new = reversed(my_list)
    for number in new:
        print("{}".format(number))
