#!/usr/bin/boithon
from collections import namedtuple,defaultdict
import re

def part_one(the_input):
    xreg = list()
    xreg.append(1) 
    cycle = 0
    pending = 0 
    for line in the_input: 
        cycle += 1
        xreg.append(pending +  xreg[cycle - 1])
        pending = 0 
        if re.match('noop', line): 
            print(f"{cycle}: {xreg[cycle]}: {line}")
        else: 
            command, num = line.split(' ')
            #skip a cycle
            print(f"{cycle}: {xreg[cycle]}: {line}")
            cycle += 1
            xreg.append(pending +  xreg[cycle - 1])
            pending = int(num)
            print(f"{cycle}: {xreg[cycle]}: {line}")
# 20th, 60th, 100th, 140th, 180th, and 220th cycles
    score = 0
    print(f" {len(xreg)}")
    for i in [20,60,100,140,180,220]: 
        print(f"{i}: {xreg[i]}")
        score += xreg[i] * i
    part_two(xreg)
    return  score

def part_two(xreg):
    cycle = 1
    for row in range(6):
        string = ""
        for col in range(1,41): 
            sprite = xreg[cycle]
            if (col - sprite  < 3) and (col - sprite  >= 0):
                string += "#"
            else: 
                string += ' '
            cycle += 1
        print(f"{string}")
    return 

if __name__ == "__main__":
    with open('10.in') as f:
        the_input = [line.rstrip() for line in f]

    part_one = part_one(the_input)
    #part_two = part_two(the_input)
    print(f"Part 1:\n{part_one}")
    #print(f"Part 2:\n{part_two}")
