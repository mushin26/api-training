#!/usr/bin/env python3
"""Infinite While Loop Example"""

x = 0

while True:
    print(f"HELP! I'M STUCK IN A WHILE LOOP AND I CAN'T GET OUT. x = {x}")
    x += 1
    if x >= 100_000:
        print("Finally breaking out of the loop!")
        break

