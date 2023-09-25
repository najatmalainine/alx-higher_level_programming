#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    for i, j in zip(my_list_1, my_list_2):
        try:
            div = i / j
        except ZeroDivisionError:
            print("division by 0")
            div = 0
        except TypeError:
            print("wrong type")
            div = 0
        finally:
            result_list.append(div)
    while len(result_list) < list_length:
        print("out of range")
        result_list.append(0)

    return result_list
