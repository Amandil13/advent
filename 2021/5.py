#!/usr/bin/boithon
import re

def part_one(the_input):
    return 


def part_two(the_input):
    return 

def draw_line(grid,start_x,start_y,end_x,end_y,diagonals): 
    #find the direction of our lines
    x_step = 0
    if start_x > end_x: 
        x_step = -1
    elif start_x < end_x: 
        x_step = 1
    y_step = 0
    if start_y > end_y: 
        y_step = -1
    elif start_y < end_y: 
        y_step = 1

    #Bail out if diaganols and they are not enabled
    if x_step != 0 and y_step != 0 and diagonals == False:
        return grid
    
    #Find how many steps
    stepcount = 0;
    if x_step != 0:
        stepcount = abs(start_x - end_x)
    else: 
        stepcount = abs(start_y - end_y)

    #draw the line now
    x = start_x
    y = start_y
    for i in range(0,stepcount + 1): 
        grid[x][y] += 1
        y += y_step
        x += x_step

    return grid

if __name__ == "__main__":
    #initialize data
    grid = list()
    gridsize = 999 
    for i in range(0,gridsize):
        row = list()
        for j in range(0,gridsize): 
            row.append(0)
        grid.append(row)

    #loop through the data
    with open('5.in') as f:
        for line in f:
            #parse the vector
            m= re.search(r"(\d+),(\d+) -> (\d+),(\d+)",line)
            start_x = int(m.group(1))
            start_y = int(m.group(2))
            end_x = int(m.group(3))
            end_y = int(m.group(4))
            draw_line(grid,start_x,start_y,end_x,end_y,True)
        
    score = 0
    for i in range(0,gridsize):
        for j in range(0,gridsize): 
            if grid[i][j] >= 2:
                score += 1

    print(f"Part 1: {score}")
