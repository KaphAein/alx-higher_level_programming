#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = [replace if x == search else x for x in row]
    return new_list