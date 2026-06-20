#!/usr/bin/python3
s = ""
for i in range(25, -1, -1):
    if i % 2 == 0:
        s += "{}".format(chr(ord('a') + i))
    else:
        s += "{}".format(chr(ord('A') + i))
print("{}".format(s), end="")
