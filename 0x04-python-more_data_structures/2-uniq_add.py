#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    uniq = list(set(my_list))
    for i in range(len(uniq)):
        sum += uniq[i]
    return sum
