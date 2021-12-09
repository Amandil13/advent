#!/usr/bin/boithon
from collections import namedtuple

def part_one(topography,drainage):
    low_points = set(list(drainage.values()))
    risk = 0
    for point in low_points: 
        risk += 1 + topography[point]
    return risk


def part_two(drainage):
    values = list(drainage.values())
    basin_sizes = list()
    for low_point in set(values): 
        basin_sizes.append(values.count(low_point))
    basin_sizes.sort()
    return basin_sizes[-1] *  basin_sizes[-2] *  basin_sizes[-3]

def find_drainage_basin(topography,drainage,point): 
    #Given a point, we need to find out where it drains. This works recursively. 
    if drainage.get(point):
        return drainage[point]
    row = point.row
    col = point.col
    height = topography[point]
    if height == 9: 
        return point
    if row > 0 and topography[Point(row - 1,col)] < height:
        basin_low = find_drainage_basin(topography,drainage,Point(row - 1,col))
        drainage[point] = basin_low
        return basin_low
    if row < 99 and topography[Point(row + 1,col)] < height:
        basin_low = find_drainage_basin(topography,drainage,Point(row + 1,col))
        drainage[point] = basin_low
        return basin_low
    if col > 0 and topography[Point(row,col - 1)] < height:
        basin_low = find_drainage_basin(topography,drainage,Point(row,col - 1))
        drainage[point] = basin_low
        return basin_low
    if col < 99 and topography[Point(row,col + 1)] < height:
        basin_low = find_drainage_basin(topography,drainage,Point(row,col + 1))
        drainage[point] = basin_low
        return basin_low

    drainage[point] = point
    return point

if __name__ == "__main__":
    the_input = list()
    Point = namedtuple('Point', ['row', 'col'])
    with open('9.in') as f:
        the_input = [line.rstrip() for line in f]
    topography = dict()
    for row in range(len(the_input)): 
        for col in range(len(the_input[row])):
            topography[Point(row,col)] = int(the_input[row][col])
    drainage = dict()
    for point in topography.keys(): 
        find_drainage_basin(topography,drainage,point)

    part_one = part_one(topography,drainage)
    part_two = part_two(drainage)
    print(f"Part 1:\n{part_one}")
    print(f"Part 2:\n{part_two}")
