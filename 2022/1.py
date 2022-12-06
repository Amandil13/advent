#!/usr/bin/boithon
from collections import namedtuple,defaultdict
import re


def import_data():
    with open('1.in') as f:
        data = [line.rstrip() for line in f]
    elves = defaultdict(int)
    num = 1
    for line in data:
        if re.match('\d+',line): 
            elves[num] += int(line)
        else:
            num += 1
    return elves

def part_one(elves):
    bestelf = 1
    for elf,calories in elves.items():
        if calories > elves[bestelf]: 
            bestelf = elf
    return elves[bestelf]

def part_two(elves):
    values = sorted(elves.values())
    print(f"Values:\n{values}")
    return values[-1] + values[-2] + values[-3]

if __name__ == "__main__":
    data = import_data();

    part_one = part_one(data)
    part_two = part_two(data)
    print(f"Part 1:\n{part_one}")
    print(f"Part 2:\n{part_two}")
