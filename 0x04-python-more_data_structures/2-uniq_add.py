#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum_result = 0
    my_set = set(my_list)
    for i in my_set:
        sum_result += i
    return sum_result
