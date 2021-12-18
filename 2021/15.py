##!/usr/bin/boithon
from collections import namedtuple,defaultdict,deque
import heapdict

#@profile
def dickstras(risk_map,start,goal):
    visited = defaultdict()
    completed = list()
    risks = defaultdict(lambda: float('inf'))
    risks[start] = 0
    totalrisks = heapdict.heapdict()
    totalrisks[start] = 0

    distance_to_goal = dict()
    for key in risk_map.keys(): 
        distance_to_goal[key] = abs(goal.row - key.row) + abs(goal.col - key.col)

    iterations = 0
    while True:
        iterations += 1 
        current_min = totalrisks.popitem()[0]
        if current_min == goal: 
            # We've Made it!
            print(f"iterations:{iterations}")
            return risks[current_min]

        for neighbor in neighbors(risk_map,current_min):
            tentative_value = risks[current_min] + risk_map[neighbor]
            if tentative_value < risks[neighbor]:
                risks[neighbor] = tentative_value
                totalrisks[neighbor] = tentative_value + distance_to_goal[neighbor]
                #totalrisks[neighbor] = tentative_value
                visited[neighbor] = current_min
    return "No path found"

def print_dick(dick): 
    for k,v in dick.items(): 
        if v != float('inf'): 
            print(f"{k}: {v}")
    
def neighbors(risk_map,point): 
    points_to_try = [
            Point(point.row,point.col + 1),
            Point(point.row + 1,point.col),
            Point(point.row,point.col - 1),
            Point(point.row - 1,point.col),
        ]
    neighbors = list()
    for p in points_to_try: 
        if p in risk_map.keys(): 
            neighbors.append(p)
    return neighbors

def part2ify(risk_map,the_input): 
    for i in range(5):
        for j in range(5): 
            for row in range(len(the_input)): 
                for col in range(len(the_input[row])):
                    value =  int(the_input[row][col]) + i + j
                    if value > 9: 
                        value -= 9
                    risk_map[Point(row + (100 * i),col + (100 * j))] = value

if __name__ == "__main__":
    the_input = list()
    Point = namedtuple('Point', ['row', 'col'])
    #with open('15.sample') as f:
    with open('15.in') as f:
        the_input = [line.rstrip() for line in f]
    risk_map = dict()
    for row in range(len(the_input)): 
        for col in range(len(the_input[row])):
            value =  int(the_input[row][col])
            risk_map[Point(row,col)] = value

    part_one = dickstras(risk_map,Point(0,0),Point(99,99))

    print(f"Part 1:\n{part_one}")
    part2ify(risk_map,the_input)
    part_two = dickstras(risk_map,Point(0,0),Point(499,499))
    print(f"Part 2:\n{part_two}")
