#!/usr/bin/python3
for alphabets in range(97, 123):
    if chr(alphabets) != 'q' and chr(alphabets) != 'e':
        print(f"{chr(alphabets)}", end="")
