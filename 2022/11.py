#!/usr/bin/boithon
from collections import namedtuple,defaultdict
import re


def part_one(monkeys):
    for i in range(10000):
        print(f"ROUND {i}: FIGHT")
        for monkey in monkeys:
            thrown = monkey.inspect_items()
            while thrown: 
                worry = thrown.pop(0)
                target = thrown.pop(0)
                monkeys[target].catch_item(worry)
        for monkey in monkeys:
            print(f"{monkey.items_inspected}")

    inspections = list()
    for monkey in monkeys:
        inspections.append(monkey.items_inspected)
        print(f"Monkey \n{monkey}")
    inspections.sort()
    return inspections[-1] * inspections[-2]

def track_item(monkeys,round_numbers): 
    #Returns a repeating pattern in which the item goes
    pattern = ""
    for i in range(round_numbers):
        i = 0
        for monkey in monkeys:
            thrown = monkey.inspect_items()
            while thrown: 
                pattern += str(i)
                worry = thrown.pop(0)
                target = thrown.pop(0)
                monkeys[target].catch_item(worry)
            i += 1
        pattern += ','

    #We have a record, now lets get the pattern
    for i in range(-2,-41,-1): 
        testpattern = pattern[i:]
        #print(f"Testing {testpattern}")
        if pattern[2*i:i] == testpattern and pattern[3*i:2*i] == testpattern and pattern[4*i:3*i] == testpattern and pattern[5*i:4*i] == testpattern and pattern[6*i:5*i] == testpattern and pattern[7*i:6*i] == testpattern and pattern[8*i:7*i] == testpattern: 
            #If pattern repeats 4 times assume it is actually stuck in a repeat 
            rounds = 20
           #print(f"Found pattern '{testpattern}' in '{pattern}'")
            while pattern.count(',') <= rounds: 
                #This can put us over...
                pattern += testpattern
            count = 0; 
            for j in range(len(pattern)): 
                if pattern[j] == ',': 
                    count += 1
                if count >= rounds: 
                    return pattern[0:j]
    return False 


def part_two(testmonkeys,monkeys):
    patterns = list()
    for monkey in testmonkeys: 
        monkey.items = list()
    for i in range(len(monkeys)): 
        for item in monkeys[i].items: 
            testmonkeys[i].catch_item(item)

            round_numbers = 40
            pattern = track_item(testmonkeys,round_numbers)
            while (not pattern): 
                for monkey in testmonkeys: 
                    monkey.items = list()
                testmonkeys[i].catch_item(item)
                round_numbers += 5
                #print(f"Doing more rounds for item {item}:{round_numbers}")
                if round_numbers >= 200: 
                    print("Giving up...")
                    break
                pattern = track_item(testmonkeys,round_numbers)

            print(f"{item}:{pattern}")
            patterns.append(pattern)
            for monkey in testmonkeys: 
                monkey.items = list()
    counts = [0,0,0,0,0,0,0,0,0]
    for pattern in patterns: 
        for i in range(8): 
            counts[i] += pattern.count(str(i))
    return counts
    counts.sort()
    return counts[-1] * counts[-2]

def parse_monkeys(the_input): 
    monkey = 0
    monkies = list() 
    while the_input: 
        line = the_input.pop(0)
        #items
        line = the_input.pop(0)
        m = re.search(r": ([\d, ]+)",line)
        items =  [int(x) for x in m.group(1).split(', ')]
        #Operation
        line = the_input.pop(0)
        m = re.search(r"= (.+)$",line)
        operation = m.group(1)
        #test
        line = the_input.pop(0)
        m = re.search(r"(\d+)",line)
        test = int(m.group(1))
        #istrue
        line = the_input.pop(0)
        m = re.search(r"(\d+)",line)
        istrue = int(m.group(1))
        #isfalse
        line = the_input.pop(0)
        m = re.search(r"(\d+)",line)
        isfalse = int(m.group(1))
        #emptyline
        if the_input: 
            line = the_input.pop(0)
        
        monkies.append(Monkey(operation,test,istrue,isfalse))
        for item in items:
            monkies[monkey].catch_item(item)

        print(f"Monkey {monkey}: \n{monkies[monkey]}\n")
        monkey += 1

    return monkies
        

class Monkey: 
    def __init__(self,operation,test,istrue,isfalse): 
        self.test = test
        self.istrue = istrue
        self.isfalse = isfalse
        self.items = list() 
        self.operation = operation
        self.items_inspected = 0

    def catch_item(self,worry):
        self.items.append(worry)
        return self.items

    def inspect_items(self):
        thrown_items = list() 
        while self.items:
            old = int(self.items.pop(0))
            self.items_inspected += 1
            old = eval(self.operation)
            #old = old // 3
            lcm = 9699690
            if old > lcm:
                old = old % lcm
            if old % self.test == 0:
                thrown_items.append(old)
                thrown_items.append(self.istrue)
            else:
                thrown_items.append(old)
                thrown_items.append(self.isfalse)
        return thrown_items

    def __str__(self):
        return f"Test: {self.test}\nTrue: {self.istrue}\nFalse: {self.isfalse}\nOperation: {self.operation}\nItems: {self.items}"
        


if __name__ == "__main__":
    with open('11.in') as f:
        the_input = [line.rstrip() for line in f]
    monkeys = parse_monkeys(the_input)

    part_one = part_one(monkeys)
    #part_two = part_two(testmonkeys,monkeys)
    print(f"Part 1:\n{part_one}")
    print(f"Part 2:\n{part_two}")
