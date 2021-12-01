#!/usr/bin/python 

def larger(listy): 
    previous = 0
    total = 0
    for s in listy:
        if previous > 0 and s > previous:
            total += 1
        previous = s
    return total


sonars = []
with open('1.in') as f:
    for line in f:
        sonars.append(int(line))
sums = []
for i in range(0,len(sonars) - 2): 
    sums.append(sonars[i] + sonars[i + 1] + sonars[i + 2])
partone = larger(sonars)
parttwo = larger(sums)
print(f"Part 1: {partone}")
print(f"part 2: {parttwo}")
