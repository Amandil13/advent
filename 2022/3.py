#!/usr/bin/boithon
from collections import namedtuple,defaultdict
import re


def part_one(the_input):
    priority = ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    score = 0
    for line in the_input: 
        bag1 = line[0:int(len(line)//2)]
        bag2 = line[int(len(line)//2):len(line)]
        print(f"{bag1}\n{bag2}")
        for char in bag1:
            if bag2.find(char) != -1: 
                score += priority.find(char)
                print(f"{char}")
                break
    return  score

def part_two(the_input):
    priority = ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    score = 0
    
    for i in range(0,len(the_input),3): 
        print(f"{the_input[i]}\n{the_input[i+1]}\n{the_input[i+2]}")
        common = list()
        for char in the_input[i]:
            if the_input[i + 1].find(char) != -1: 
                common.append(char)
        for char in common: 
            if the_input[i + 2].find(char) != -1: 
                score += priority.find(char)
                print(f"{char}")
                break
    return  score

if __name__ == "__main__":
    with open('3.in') as f:
        the_input = [line.rstrip() for line in f]

    part_one = part_one(the_input)
    part_two = part_two(the_input)
    print(f"Part 1:\n{part_one}")
    print(f"Part 2:\n{part_two}")
