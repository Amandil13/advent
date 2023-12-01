#!/usr/bin/boithon
from collections import namedtuple,defaultdict
import re


def import_data():
    with open('1.in') as f:
        data = [line.rstrip() for line in f]
    return data

def part_one(data):
    total = 0
    for line in data:
        for i in (line):
            if i.isdigit():
                first = i
                break
        for i in (line[::-1]):
            if i.isdigit():
                last = i
                break
        #print(f"found {first},{last} in {line}")
        value = first + last
        total += int (value)
    return total


def part_two(data):
    total = 0
    for line in data:
        liner = line.replace("one","one1")
        liner = liner.replace("two","two2")
        liner = liner.replace("three","three3")
        liner = liner.replace("four","four4")
        liner = liner.replace("five","five5")
        liner = liner.replace("six","six6")
        liner = liner.replace("seven","seven7")
        liner = liner.replace("eight","eight8")
        liner = liner.replace("nine","nine9")
        for i in (liner):
            if i.isdigit():
                first = i
                break
        linel = line.replace("one","1one")
        linel = linel.replace("two","2two")
        linel = linel.replace("three","3three")
        linel = linel.replace("four","4four")
        linel = linel.replace("five","5five")
        linel = linel.replace("six","6six")
        linel = linel.replace("seven","7seven")
        linel = linel.replace("eight","8eight")
        linel = linel.replace("nine","9nine")
        for i in (linel[::-1]):
            if i.isdigit():
                last = i
                break
        print(f"found {first},{last} in {line}")
        value = first + last
        total += int (value)
    return total

if __name__ == "__main__":
    data = import_data()
    part_one = part_one(data)
    part_two = part_two(data)
    print(f"Part 1:\n{part_one}")
    print(f"Part 2:\n{part_two}")
