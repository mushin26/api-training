#!/usr/bin/env python3
"""While Loop with Break"""

x = 0

while x < 10:
    x += 1
    print("The value of x is now:", x)
    if x == 5:
        print("Breaking the loop early!")
        break

print("The while loop is now finished.")

