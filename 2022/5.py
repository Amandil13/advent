#!/usr/bin/boithon
from collections import namedtuple,defaultdict
import re


def part_one(crates,instructions):
    for line in instructions: 
        split = line.split(' ')
        count = int(split[1])
        source = int(split[3])
        dest = int(split[5])
        for i in range(count): 
            crates[dest - 1].append(crates[source - 1].pop())
            #print(f"{crates}")
    answer = ""
    for i in range(9): 
        answer += crates[i][-1]
    return answer

def part_two(crates,instructions):
    for line in instructions: 
        for i in range(9):
            print(f"{i}:{crates[i]}")
        print("")
        split = line.split(' ')
        count = int(split[1])
        source = int(split[3])
        dest = int(split[5])
        #Why slice when we can just use two cratemover 9000's? 
        temp = list()
        for i in range(count): 
            temp.append(crates[source - 1].pop())
        while (temp): 
            crates[dest - 1].append(temp.pop())
    answer = ""
    for i in range(9): 
        answer += crates[i][-1]
    return answer

def parse_crates(the_input): 
    crates = list() 
    for i in range(9): 
        crates.append(list())
    the_input.reverse()
    for line in the_input: 
        for i in range(9): 
            if (line[ i*4 + 1 ]) != ' ': 
                crates[i].append(line[ i*4 + 1 ])
    #print(f"{crates}")
    return crates

if __name__ == "__main__":
    with open('5.crates') as f:
        the_crates = [line.rstrip() for line in f]
    crates = parse_crates(the_crates)
    crates2 = parse_crates(the_crates)

    with open('5.in') as f:
        instructions = [line.rstrip() for line in f]

    part_one = part_one(crates.copy(),instructions)
    part_two = part_two(crates2,instructions)
    print(f"Part 1:\n{part_one}")
    print(f"Part 2:\n{part_two}")
