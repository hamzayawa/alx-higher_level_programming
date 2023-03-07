#!/usr/bin/python3
for alphabets in range(97, 123):
    if chr(alphabets) is not 'q' and chr(alphabets) is not 'e':
        print("{}".format(chr(alphabets)), end="")
