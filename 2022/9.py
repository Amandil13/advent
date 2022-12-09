#!/usr/bin/boithon
from collections import namedtuple,defaultdict

def part_one(the_input,grid):
    head = Point(0,0)
    tail = Point(0,0)
    grid[tail] += 1

    for line in the_input: 
        direction,distance = line.split(' ')

        if direction == 'R':
            for i in range(int(distance)):
                head = Point(head[0],head[1] + 1)
                tail = check_knot(head,tail,grid)

        if direction == 'L':
            for i in range(int(distance)):
                head = Point(head[0],head[1] - 1)
                tail = check_knot(head,tail,grid)

        if direction == 'U':
            for i in range(int(distance)):
                head = Point(head[0] + 1,head[1])
                tail = check_knot(head,tail,grid)

        if direction == 'D':
            for i in range(int(distance)):
                head = Point(head[0] - 1,head[1])
                tail = check_knot(head,tail,grid)

    values = list(grid.values())
    return len( values)

def part_two(the_input):
    rope  = list()
    realgrid = defaultdict(int)
    dummygrid = defaultdict(int)
    for i in range(10): 
        rope.append(Point(0,0))
    realgrid[rope[9]] += 1

    for line in the_input: 
        direction,distance = line.split(' ')

        if direction == 'R':
            for i in range(int(distance)):
                rope[0] = Point(rope[0][0],rope[0][1] + 1)
                grid = dummygrid
                for i in range(1,10): 
                    if i == 9:
                        grid = realgrid
                    rope[i] = check_knot(rope[i - 1],rope[i],grid)

        if direction == 'L':
            for i in range(int(distance)):
                rope[0] = Point(rope[0][0],rope[0][1] - 1)
                grid = dummygrid
                for i in range(1,10): 
                    if i == 9:
                        grid = realgrid
                    rope[i] = check_knot(rope[i - 1],rope[i],grid)

        if direction == 'U':
            for i in range(int(distance)):
                rope[0] = Point(rope[0][0] + 1,rope[0][1])
                grid = dummygrid
                for i in range(1,10): 
                    if i == 9:
                        grid = realgrid
                    rope[i] = check_knot(rope[i - 1],rope[i],grid)

        if direction == 'D':
            for i in range(int(distance)):
                rope[0] = Point(rope[0][0] - 1,rope[0][1])
                grid = dummygrid
                for i in range(1,10): 
                    if i == 9:
                        grid = realgrid
                    rope[i] = check_knot(rope[i - 1],rope[i],grid)

    values = list(realgrid.values())
    return len( values)

def check_knot(head,tail,grid): 
    row_offset = head[0] - tail[0]
    col_offset = head[1] - tail[1]
    if abs(row_offset) <= 1 and abs(col_offset) <= 1: 
        return tail
    if row_offset > 0: 
        row_offset = 1
    if row_offset < 0: 
        row_offset = -1
    if col_offset > 0: 
        col_offset = 1
    if col_offset < 0: 
        col_offset = -1
    tail = Point(tail[0] + row_offset,tail[1] + col_offset)
    grid[tail] += 1
    return tail

if __name__ == "__main__":
    the_input = list()
    Point = namedtuple('Point', ['row', 'col'])
    with open('9.in') as f:
        for line in f: 
            the_input.append(line)
    grid = defaultdict(int)


    part_one = part_one(the_input,grid)
    part_two = part_two(the_input)
    print(f"Part 1:\n{part_one}")
    print(f"Part 2:\n{part_two}")
