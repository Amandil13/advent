##!/usr/bin/boithon
from collections import namedtuple,defaultdict,deque
import heapdict
import re

class Scanner: 
    def __init__(self,name): 
        self.points = [[],[],[],]
        self.absolute_position = None
        self.name = name

    def add_point(self,x,y,z): 
        self.points[0].append(x)
        self.points[1].append(y)
        self.points[2].append(z)

    def flip_axis(self,axis): 
        #I think I need to do some right hand rule schenangigans...but for now we are just gonna flip and go 
        for i in range(len(self.points[axis])): 
            self.points[axis][i] *= -1


def flip(axis): 
    for i in range(len(axis)): 
        axis[i] *= -1
    return axis

def find_matches(axis_one, axis_two): 
    number_of_matches = 0
    for i in axis_one: 
        if i in axis_two: 
            number_of_matches += 1
    return number_of_matches

def compare_axis(axis_one,axis_two): 
    for i in range(len(axis_one)): 
        for j in range(len(axis_two)):
            offset = axis_one[i] - axis_two[j]
            adjusted_axis = list()
            for k in axis_two:
                adjusted_axis.append(k + offset)
            if (find_matches(adjusted_axis,axis_one) >= 12): 
                return [offset,axis_one[i],axis_two[j]]
    return [None,None,None]

def find_scanner_neighbor(parent_scanner,scanners,initial_axis): 
    search_axis = sorted(parent_scanner.points[initial_axis])
    neighbors = list() 
    for scanner in scanners: 
        if scanner.name == parent_scanner.name:
            continue
        points = scanner.points
        for axis in range(len(scanner.points)): 
            #print(f"NEXT SCANNER: {scanner.points[axis]}")
            match_axis = sorted(scanner.points[axis])
            offset,p1,p2 = compare_axis(search_axis,match_axis)
            if offset != None and scanner.absolute_position == None: 
                print(f"MATCH FOUND\noffset: {offset}\nscanner: {scanner.name}\naxis: {axis}")
                index = scanner.points[axis].index(x)


                offset + parent_scanner.absolute_position[initial_axis]

                scanner.absolute_position = [offset + parent_scanner.absolute_position[initial_axis],0,0]
                neighbors.append(scanner)
            match_axis = flip(sorted(scanner.points[axis]))
            offset,p1,p2 = compare_axis(search_axis,match_axis)
            if offset != None and scanner.absolute_position == None: 
                print(f"FLIPPED MATCH FOUND\noffset: {offset}\nscanner: {scanner.name}\naxis: {axis}")
                scanner.absolute_position = [offset + parent_scanner.absolute_position[initial_axis],0,0]
                neighbors.append(scanner)
    return neighbors



if __name__ == "__main__":
    the_input = list()
    Point = namedtuple('Point', ['x', 'y','z'])

    scanners = list()
    with open('19.in') as f:
        scanner = None
        i = 0
        for line in f: 
            line.strip()
            if "scanner" in line: 
                if scanner != None: 
                    scanners.append(scanner)
                print(f"new scanner {i}")
                scanner = Scanner(i)
                i += 1
            if m := re.match('(.*),(.*),(.*)',line): 
                scanner.add_point(int(m.group(1)),int(m.group(2)),int(m.group(3)))
        scanners.append(scanner)

    scanners[0].absolute_position = [0,0,0]
    queue = list() 
    queue.append(scanners[0])
    while len(queue) > 0: 
        scanner = queue.pop(0)
        print(f"finding position for: {scanner.name}")
        queue.extend(find_scanner_neighbor(scanner,scanners,0))
