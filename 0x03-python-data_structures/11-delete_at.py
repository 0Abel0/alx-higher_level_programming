#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    for n, j in enumerate(my_list):
        if n == idx:
            my_list.remove(j)
    return my_list
