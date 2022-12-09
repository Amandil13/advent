#!/usr/bin/boithon
from collections import namedtuple

def part_one(forest):
    visible = dict()
    bound = 98

    for col in range(bound + 1): 
        row = bound 
        visible[Point(row,col)] = 1
        highest = forest[Point(row,col)]
        while Point(row - 1,col) in forest.keys():
            row = row - 1
            if forest[Point(row,col)] > highest: 
                visible[Point(row,col)] = 1
                highest = forest[Point(row,col)]

    for col in range(bound + 1): 
        row = 0
        visible[Point(row,col)] = 1
        highest = forest[Point(row,col)]
        while Point(row + 1,col) in forest.keys():
            row = row + 1
            if forest[Point(row,col)] > highest: 
                visible[Point(row,col)] = 1
                highest = forest[Point(row,col)]

    for row in range(bound + 1): 
        col = bound 
        visible[Point(row,col)] = 1
        highest = forest[Point(row,col)]
        while Point(row,col - 1) in forest.keys():
            col = col - 1
            if forest[Point(row,col)] > highest: 
                visible[Point(row,col)] = 1
                highest = forest[Point(row,col)]

    for row in range(bound + 1): 
        col = 0
        visible[Point(row,col)] = 1
        highest = forest[Point(row,col)]
        while Point(row,col + 1) in forest.keys():
            col = col + 1
            if forest[Point(row,col)] > highest: 
                visible[Point(row,col)] = 1
                highest = forest[Point(row,col)]

    return len(visible)


def part_two(forest):
    best_vantage = 0;
    best_tree = Point(0,0)
    for tree in forest.keys():
        vantage = score_tree(forest,tree)
        if vantage > best_vantage: 
            best_tree = tree
            best_vantage = vantage
    print(f"Best Tree: {best_tree}")
    return best_vantage

def score_tree(forest,tree): 
    score = 1;
    for step in [1,-1]: 
        vantage = 0
        height = forest[tree]
        row = tree[0]
        col = tree[1]
        while Point(row + step,col) in forest.keys():
            row = row + step
            vantage += 1
            if forest[Point(row,col)] >= height:
                break
        score *= vantage

    for step in [1,-1]: 
        vantage = 0
        height = forest[tree]
        row = tree[0]
        col = tree[1]
        while Point(row,col + step) in forest.keys():
            col = col + step
            vantage += 1
            if forest[Point(row,col)] >= height:
                break
        score *= vantage

    return score


if __name__ == "__main__":
    the_input = list()
    Point = namedtuple('Point', ['row', 'col'])
    with open('8.in') as f:
        the_input = [line.rstrip() for line in f]
    forest = dict()
    for row in range(len(the_input)): 
        for col in range(len(the_input[row])):
            forest[Point(row,col)] = int(the_input[row][col])

    part_one = part_one(forest)
    part_two = part_two(forest)
    print(f"Part 1:\n{part_one}")
    print(f"Part 2:\n{part_two}")
