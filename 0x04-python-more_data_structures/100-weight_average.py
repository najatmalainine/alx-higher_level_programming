#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    sum_sc = 0
    total_weight = 0
    for i, j in my_list:
        sum_sc += i * j
        total_weight += j
    if total_weight == 0:
        return 0
    result = sum_sc / total_weight
    return result
