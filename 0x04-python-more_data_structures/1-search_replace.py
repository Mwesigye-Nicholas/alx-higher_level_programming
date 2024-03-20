#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list[:]
    for index, items in enumerate(new_list):
        if items == search:
            new_list[index] = replace
    return new_list
