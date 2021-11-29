#!/usr/bin/env python3
import re
import sys

def validate_password_part2(line): 
    m = re.search(r"(\d+)-(\d+) (\w): (\w+)", line)
    minimum = int(m.group(1)) - 1
    maximum = int(m.group(2)) - 1
    pattern = m.group(3)
    password = m.group(4)
    count = password.count(pattern)
    if (bool(password[minimum] == pattern) ^ bool(password[maximum] == pattern)):
        print(f"{password}")
        return 1
    else:
        return 0

def validate_password_part1(line): 
    m = re.search(r"(\d+)-(\d+) (\w): (\w+)", line)
    minimum = int(m.group(1))
    maximum = int(m.group(2))
    pattern = m.group(3)
    password = m.group(4)

    count = password.count(pattern)
    if count >= minimum and count <= maximum:
        print(f"{password}")
        return 1
    else:
        return 0 

total = 0
with open('2.in') as f:
    for line in f:
        total += validate_password_part2(line)
print(f"{total}")
