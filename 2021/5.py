#!/usr/bin/boithon


import re
from collections import defaultdict,namedtuple


def part_one(vectors):
    grid = defaultdict(int)
    for vector in vectors:  
        draw_line(grid,vector,False)
    return score_grid(grid)

def part_two(vectors):
    grid = defaultdict(int)
    for vector in vectors:  
        draw_line(grid,vector,True)
    return score_grid(grid)

def draw_line(grid,vector,diagonals): 
    #Negated compare to find the direction of our lines
    x_step = (vector[0].x < vector[1].x) - (vector[0].x > vector[1].x)
    y_step = (vector[0].y < vector[1].y) - (vector[0].y > vector[1].y)

    #Bail out if diaganols and they are not enabled
    if x_step != 0 and y_step != 0 and diagonals == False:
        return grid
    
    #Find how many steps
    stepcount = max(abs(vector[0].x - vector[1].x),abs(vector[0].y - vector[1].y))

    #draw the line now
    x = vector[0].x
    y = vector[0].y
    for i in range(0,stepcount + 1): 
        grid[Point(x,y)] += 1
        y += y_step
        x += x_step

    return grid

def score_grid(grid): 
    values = list(grid.values())
    return len(grid) - values.count(1)


if __name__ == "__main__":
    Point = namedtuple('Point', ['x', 'y'])
    vectors = list()

    #parse the data
    with open('5.in') as f:
        for line in f:
            #parse the vector
            m= re.search(r"(\d+),(\d+) -> (\d+),(\d+)",line)
            vector = (Point(int(m.group(1)),int(m.group(2))),Point(int(m.group(3)),int(m.group(4))))
            vectors.append(vector)

    part_one = part_one(vectors)
    print(f"Part 1:\n{part_one}")
    part_two = part_two(vectors)
    print(f"Part 2:\n{part_two}")
