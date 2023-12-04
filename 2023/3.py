#!/usr/bin/boithon
from collections import namedtuple,defaultdict


dimensions = 140
def part_one(schematic):
    is_a_part = 0
    total = 0
    gears = {}
    total_gears = defaultdict(int)
    total_gears_ratio = defaultdict(lambda: 1)
    for i in (range(dimensions)): 
        print(f"Row {i}:")
        current_number = ""
        for j in (range(dimensions)): 
            if schematic[Point(i,j)].isdigit():
                current_number = "" + current_number + schematic[Point(i,j)]
                is_a_part += int(is_next_to_symbol(schematic,i,j))
                find_adjacent_gears(schematic,i,j,gears)
            if (not schematic[Point(i,j)].isdigit()) or j + 1 >= dimensions: 
                if is_a_part > 0:
                    print(f"#{current_number} : {is_a_part}")
                    if current_number: 
                        total += int(current_number)
                        for gear in gears.keys(): 
                            total_gears[gear] += 1
                            total_gears_ratio[gear] *= int(current_number)
                is_a_part = 0
                current_number = "" 
                gears = {} 
    part_two = 0
    for gear,count in total_gears.items(): 
        if count != 2: 
            continue
        part_two += total_gears_ratio[gear]
    print(f"P2: {part_two}")

    return total
        
def is_next_to_symbol(schematic,x,y): 
    for i in [-1,0,1]: 
        if x + i < 0 or x + i >= dimensions:
            continue
        for j in [-1,0,1]: 
            if y + j < 0 or y + j >= dimensions:
                continue
            if not schematic[Point(x + i,y + j)].isdigit() and schematic[Point(x + i,y + j)] != ".":
                return 1
    return 0

def find_adjacent_gears(schematic,x,y,gears): 
    for i in [-1,0,1]: 
        if x + i < 0 or x + i >= dimensions:
            continue
        for j in [-1,0,1]: 
            if y + j < 0 or y + j >= dimensions:
                continue
            if schematic[Point(x + i,y + j)] == "*":
                gears[Point(x + i,y + j)] = 1
    return gears

def part_two(the_input):
    return 0

if __name__ == "__main__":
    the_input = list()
    Point = namedtuple('Point', ['row', 'col'])
    grid = {}
    with open('3.in') as f:
        the_input = [line.rstrip() for line in f]
    dimensions = len(the_input)

    for row in range(len(the_input)):
        for col in range(len(the_input[row])):
            grid[Point(row,col)] = the_input[row][col]
    #print(f"{grid}")


    part_one = part_one(grid)
    part_two = part_two(grid)
    print(f"Part 1:\n{part_one}")
    print(f"Part 2:\n{part_two}")
