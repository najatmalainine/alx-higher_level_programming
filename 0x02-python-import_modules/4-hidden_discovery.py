#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    filt_list = [i for i in dir(hidden_4) if not i.startswith('__')]
    filt_list.sort()
    for i in filt_list:
        print(i)
