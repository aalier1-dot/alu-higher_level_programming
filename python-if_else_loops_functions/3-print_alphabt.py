#!/usr/bin/python3
s = ""
for i in range(26):
    if chr(ord('a') + i) != 'q' and chr(ord('a') + i) != 'e':
        s += chr(ord('a') + i)
print(s, end="")
