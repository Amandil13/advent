#!/usr/bin/boithon
from collections import namedtuple,defaultdict
import re


def part_one(the_input):
    redundantelves = 0
    for line in the_input: 
        elves = list() 
        for elf in line.split(','): 
            elves.append( [int(x) for x in elf.split('-')] )
        #Lets find the elf that has the lowest range
        smolelf = list() 
        thiccelf = list()
        if elves[0][1] - elves[0][0] > elves[1][1] - elves[1][0]:
            smolelf = elves[1]
            thiccelf = elves[0]
        else:
            smolelf = elves[0]
            thiccelf = elves[1]

        if smolelf[0] >= thiccelf[0] and smolelf[1] <= thiccelf[1]: 
            redundantelves += 1
    return redundantelves

def part_two(the_input):
    redundantelves = 0
    for line in the_input: 
        elves = list() 
        for elf in line.split(','): 
            elves.append( [int(x) for x in elf.split('-')] )
        #Lets find the elf that has the lowest range
        smolelf = list() 
        thiccelf = list()
        if elves[0][0] < elves[1][0]:
            smolelf = elves[0]
            thiccelf = elves[1]
        else:
            smolelf = elves[1]
            thiccelf = elves[0]
        if smolelf[1] >= thiccelf[0] or smolelf[0] == thiccelf[0]: 
            redundantelves += 1
    return redundantelves

if __name__ == "__main__":
    with open('4.in') as f:
        the_input = [line.rstrip() for line in f]

    part_one = part_one(the_input)
    part_two = part_two(the_input)
    print(f"Part 1:\n{part_one}")
    print(f"Part 2:\n{part_two}")
