#!/usr/bin/python3
#1-search_replace.py
#Tsedalu ashenafi<Tseexashu08@github.com>

def search_replace(my_list, search, replace):
    """replaces all occurrences of an element by another in a new list."""
    new_list = []
    for x in range(len(my_list)):
        if my_list[x] == search:
            new_list.append(replace)
        else:
            new_list.append(my_list[x])
    return new_list
