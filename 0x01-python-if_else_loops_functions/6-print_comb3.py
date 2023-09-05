#!/usr/bin/python3
for i in range(0, 10):
    for j in range(i + 1, 10):
        if i != j:
            print("{}".format(i), end="")
            print("{}".format(j), end="\n" if i == 8 else ", ")
