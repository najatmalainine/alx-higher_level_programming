#!/usr/bin/python3
for c, d in zip(range(ord('z'), ord('a') - 1, -2),
                range(ord('Y'), ord('A') - 1, -2)):
    print("{:c}{:c}".format(c, d), end='')
