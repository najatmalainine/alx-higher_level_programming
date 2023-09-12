#!/usr/bin/python3
def max_integer(my_list=[]):
    max = my_list[0]
    if not my_list:
        return None
    else:
        for i in range(0, len(my_list)):
            if my_list[i] > max:
                max = my_list[i]
        return max
