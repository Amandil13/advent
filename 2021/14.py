#!/usr/bin/boithon
from collections import defaultdict

def part_one(recipe,molecule):
    for i in range(10): 
        print(f"{i}")
        molecule = elongate(recipe,molecule)
        #print(f"{molecule}")

    biggest = 0
    smallest = 999999
    for i in set(molecule): 
        count = molecule.count(i)
        if count > biggest: 
            biggest = count
        if count < smallest: 
            smallest = count
    return biggest - smallest

def elongate(recipe,molecule):
    new_molecule = list()
    last = ""
    for i in molecule: 
        if last == "": 
            last = i
            new_molecule.append(i)
            continue
        key = "" + last + i
        new_molecule.append(recipe[key])
        last = i
        new_molecule.append(i)
    return new_molecule
        

def part_two(recipe,molecule):
    last = ""
    combo_counts = dict()
    molecule = elongate_20(recipe,molecule)
    total_counts = defaultdict(int)
    for m in molecule: 
        if last == "": 
            total_counts[m] += 1
            last = m
            continue
        short_molecule = (last, m)
        if short_molecule not in combo_counts.keys(): 
            combo_molecule = elongate_20(recipe, [last,m])
    #        print(f"{combo_molecule}")
            counts = dict()
            for j in set(combo_molecule): 
                counts[j] = combo_molecule.count(j)
            counts[last] -= 1
            combo_counts[short_molecule] = counts
        for key,value in combo_counts[short_molecule].items(): 
            total_counts[key] += value
        last = m


    for key,value in combo_counts.items():
        print(f"{key}: {value}")
    for key,value in total_counts.items():
        print(f"{key}: {value}")
    biggest = 0
    smallest = 999999999999999
    for key,value in total_counts.items():
        if value > biggest: 
            biggest = value
        if value < smallest: 
            smallest = value

    return biggest - smallest
    

def elongate_20(recipe,molecule): 
    print(f"elongating {molecule}")
    for i in range(20): 
        molecule = elongate(recipe,molecule)
    return molecule



if __name__ == "__main__":
    the_input = list()


    recipe = dict()
    with open('14.in') as f:
        start_molecule = list()
        start_molecule[:0] = f.readline().rstrip()
        for line in f:
            if '->' not in line:
                continue
            split_line = line.rstrip().split(' -> ')
            recipe[split_line[0]] = split_line[1]


    print(f"{recipe}")
    print(f"{start_molecule}")

    the_input = 0
    part_one = part_one(recipe,start_molecule.copy())
    part_two = part_two(recipe,start_molecule)
    print(f"Part 1: {part_one}")
    print(f"Part 2: {part_two}")
