#!/usr/bin/boithon
from collections import namedtuple,defaultdict


def part_one(paper):
    paper = fold_x(paper,655)
    #print_paper(paper)
    #return sum(paper.values())
    paper = fold_y(paper,447)
    paper = fold_x(paper,327)
    paper = fold_y(paper,223)
    paper = fold_x(paper,163)
    paper = fold_y(paper,111)
    paper = fold_x(paper,81)
    paper = fold_y(paper,55)
    paper = fold_x(paper,40)
    paper = fold_y(paper,27)
    paper = fold_y(paper,13)
    paper = fold_y(paper,6)
    print_paper(paper)
    return

def fold_x(paper,x):
    new_paper = defaultdict(int)
    for point,value in paper.items(): 
        if value == 0: 
            continue
        if point.x > x: 
            new_paper[Point(x - (point.x - x), point.y)] = 1
        else: 
            new_paper[point] = 1
    return new_paper

def fold_y(paper,y): 
    new_paper = defaultdict(int)
    for point,value in paper.items(): 
        if value == 0: 
            continue
        if point.y > y: 
            new_paper[Point(point.x,y - (point.y - y))] = 1
        else: 
            new_paper[point] = 1
    return new_paper

def part_two(octopi):
    return "1000 cycles and no end?"

def print_paper(paper): 
    exes = list()
    whys = list()
    print("-------------------------------------------------")
    for point in paper.keys(): 
        exes.append(point.x)
        whys.append(point.y)
    for y in range(max(whys) + 1): 
        string = ""
        for x in range(max(exes) + 1): 
            if paper[Point(x,y)] == 0: 
                string += " "
            else:
                string += "#"
#            string += str(paper[Point(x,y)])
        print(f"{string}")






if __name__ == "__main__":
    the_input = list()
    Point = namedtuple('Point', ['x', 'y'])
    paper = defaultdict(int)
    with open('13.in') as f:
        for line in f: 
            x,y = line.rstrip().split(',')
            paper[Point(int(x),int(y))] = 1


    part_one = part_one(paper.copy())
#    part_two = part_two(octopi)
    print(f"Part 1:\n{part_one}")
#    print(f"Part 2:\n{part_two}")
