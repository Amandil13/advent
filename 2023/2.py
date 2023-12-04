#!/usr/bin/boithon
from collections import namedtuple,defaultdict
import re


def import_data():
    i = 1
    rounds = {}
    with open('2.in') as f:
        data = [line.rstrip() for line in f]
        for line in data:
            rounds[i] = {}
            x = 0
            for j in line.split(';'): 
                rounds[i][x] = {}
                for k in j.split(','): 
                    m = re.match(r"\s*(\d+)\s(\w+)",k)
                    color = str(m.group(2))
                    count = int(m.group(1))
                    print(f"round {i} {color}: {count}")
                    rounds[i][x][color] = count
                x = x + 1
            i = i + 1
    #Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
    return rounds

def part_one(data):
    maxes = {'red': 12, 'green': 13, 'blue': 14}
    total = 0
    for index,value in data.items(): 
        bad = 0
        for rounds,v2 in value.items(): 
            for color,count in v2.items():
                if count > maxes[color]:
                    bad = 1
        if bad == 0: 
            print(f"rount {index} passed: {value}")
            total += index
    return total


def part_two(data):
    total = 0
    for index,value in data.items(): 
        mins = defaultdict(int)
        for rounds,v2 in value.items(): 
            for color,count in v2.items():
                if count > mins[color]:
                    mins[color] = count
        power = 1
        for i,v in mins.items(): 
            power = power * v
        print(f"rount {index} powers: {power}")
        total = power + total
    return total

if __name__ == "__main__":
    data = import_data()
    print(f"{data}")
    part_one = part_one(data)
    part_two = part_two(data)
    print(f"Part 1:\n{part_one}")
    print(f"Part 2:\n{part_two}")
