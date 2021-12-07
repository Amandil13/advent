#!/usr/bin/boithon
from statistics import median

def calculate_fuel_one(crabs,position): 
    fuel = 0
    for crab in crabs: 
        fuel += int(abs(crab - position))
    return fuel
        
def calculate_fuel_two(crabs,position_wanted): 
    fuel = 0
    for crab in crabs: 
        units_away = int(abs(crab - position_wanted))
        fuel += int(units_away * units_away / 2 + units_away / 2)
    return fuel

def search_for_best_fuel(crabs,increment,guess,fuel_function):
    best_fuel = fuel_function(crabs,guess)
    test_fuel = fuel_function(crabs,guess + increment) 
    while test_fuel < best_fuel: 
        best_fuel = test_fuel
        guess = guess + increment
        test_fuel = fuel_function(crabs,guess + increment) 
    print(f"best spot for {increment} is {guess}")
    return best_fuel

if __name__ == "__main__":
    the_input = list()
    crabs = list() 
    with open('7.in') as f:
        for line in f.read().rstrip().split(','):
            crabs.append(int(line))

    #These are good gueses to start with
    median = median(crabs)
    average = int(round(sum(crabs)/len(crabs),0))
    print(f"Average: {average}")

    best_fuel_part_one = min(search_for_best_fuel(crabs,1,median,calculate_fuel_one), search_for_best_fuel(crabs,-1,median,calculate_fuel_one))
    best_fuel_part_two = min(search_for_best_fuel(crabs,1,average,calculate_fuel_two), search_for_best_fuel(crabs,-1,average,calculate_fuel_two))

    print(f"Part one: {best_fuel_part_one}")
    print(f"Part two: {best_fuel_part_two}")

