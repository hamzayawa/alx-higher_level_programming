#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    copy = a_dictionary.copy()
    for i in copy:
        if copy[i] == value:
            del a_dictionary[i]
    return a_dictionary
