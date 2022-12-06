#!/usr/bin/boithon
from collections import namedtuple,defaultdict
import re

def import_data(): 
    data = []
    key = { 
            'A':'r',
            'B':'p',
            'C':'s',
            'X':'r',
            'Y':'p',
            'Z':'s',
            }
    with open('2.in') as f:
        for line in f: 
            m = re.search(r"(\w)\s+(\w)",line)
            data.append(rps(key[m.group(1)],key[m.group(2)]))
    return data

def part_one(data):
    score = 0
    for bout in data:
        score += bout.scorewinner()
    return score

def part_two():
    data = []
    key = { 
            'A':'r',
            'B':'p',
            'C':'s',
            }
    key2 = { 
            'A':{'X':'s','Y':'r','Z':'p'},
            'B':{'X':'r','Y':'p','Z':'s'},
            'C':{'X':'p','Y':'s','Z':'r'},
            }
    with open('2.in') as f:
        for line in f: 
            m = re.search(r"(\w)\s+(\w)",line)
            data.append(rps(key[m.group(1)],key2[m.group(1)][m.group(2)]))
    score = 0
    for bout in data:
        score += bout.scorewinner()
    return score
    return 

class rps:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def scorewinner(self):
        if self.p1 == 'r':
            if self.p2 == 'r':
                return 4
            elif self.p2 == 'p': 
                return 8
            elif self.p2 == 's':
                return 3
        elif self.p1 == 'p':
            if self.p2 == 'r':
                return 1
            elif self.p2 == 'p': 
                return 5
            elif self.p2 == 's':
                return 9
        elif self.p1 == 's':
            if self.p2 == 'r':
                return 7
            elif self.p2 == 'p': 
                return 2
            elif self.p2 == 's':
                return 6

    def __str__(self):
        return f"{self.p1}:{self.p2}"


if __name__ == "__main__":
    data = import_data()

    part_one = part_one(data)
    part_two = part_two()
    #print(f"Part 1:\n{data}")
    print(f"Part 1:\n{part_one}")
    print(f"Part 2:\n{part_two}")
