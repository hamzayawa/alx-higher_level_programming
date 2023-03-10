#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    if my_list:
        reversed_list = reversed(my_list)
        for i in reversed_list:
            print("{:d}".format(i))
