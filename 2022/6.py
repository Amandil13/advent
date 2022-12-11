#!/usr/bin/boithon
from collections import namedtuple,defaultdict


def find_marker(the_input,unique):
    line = the_input[0]
    for i in range(4096): 
        chars = defaultdict(int)
        for j in range(i,i+unique): 
            chars[line[j]] += 1
        if len(chars.keys()) == unique: 
            return i + unique
    return 

if __name__ == "__main__":
    with open('6.in') as f:
        the_input = [line.rstrip() for line in f]

    part_one = find_marker(the_input,4)
    part_two = find_marker(the_input,14)
    print(f"Part 1:\n{part_one}")
    print(f"Part 2:\n{part_two}")
