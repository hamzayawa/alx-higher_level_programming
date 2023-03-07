#!/usr/bin/python3

for rev in range(122, 96, -1):
    if rev % 2 != 0:
        print("{}".format(chr(rev - 32)), end="")
    else:
        print("{}".format(chr(rev)), end="")
