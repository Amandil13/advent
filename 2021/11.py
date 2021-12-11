#!/usr/bin/boithon
from collections import namedtuple,defaultdict


def part_one(octopi):
    flashes = defaultdict(int)
    total_flashes = 0
    for i in range(100): 
        for point in octopi.keys(): 
            power_up(octopi,point,flashes)
        for point,flashed in flashes.items(): 
            if flashed == 1:
                octopi[point] = 0
                flashes[point] = 0
                total_flashes += 1

    return total_flashes

def part_two(octopi):
    flashes = defaultdict(int)
    for i in range(9999): 
        all_flashed = 1
        for point in octopi.keys(): 
            power_up(octopi,point,flashes)
        for point,flashed in flashes.items(): 
            if flashed == 1:
                octopi[point] = 0
                flashes[point] = 0
            else: 
                all_flashed = 0
        if all_flashed == 1 and len([*flashes.keys()]) == len([*octopi.keys()]):
            return i + 1
    return "1000 cycles and no end?"

def print_octopi(octopi): 
    values = list(octopi.values())
    string = ""
    for i in range(100): 
        if i % 10 == 0: 
            string += "\n"
        string += str(values[i])
    print(f"{string}")

def power_up(octopi,point,flashes): 
    octopi[point] += 1
    if octopi[point] >= 10 and flashes[point] == 0: 
        flash_neighbors(octopi,point,flashes)

def flash_neighbors(octopi,point,flashes): 
    #( • )( • )
    flashes[point] = 1
    for x in (-1,0,1): 
        for y in (-1,0,1): 
            if x == 0 and y == 0: 
                continue
            neighbor = Point(point.row + x,point.col + y) 
            if neighbor in octopi.keys(): 
                power_up(octopi,neighbor,flashes)

if __name__ == "__main__":
    the_input = list()
    Point = namedtuple('Point', ['row', 'col'])
    #with open('11.sample') as f:
    with open('11.in') as f:
        the_input = [line.rstrip() for line in f]
    octopi = dict()
    for row in range(len(the_input)): 
        for col in range(len(the_input[row])):
            octopi[Point(row,col)] = int(the_input[row][col])

    part_one = part_one(octopi.copy())
    part_two = part_two(octopi)
    print(f"Part 1:\n{part_one}")
    print(f"Part 2:\n{part_two}")
