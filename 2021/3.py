#!/usr/bin/boithon

def part_one(the_input):
    totals = dict()
    for i in range(12):
        totals[i] = 0;
    for line in the_input:
        for i in range(12):
            totals[i] += int(line[i])
    gamma = 0
    epsilon = 0
    size = len(the_input)
    binary = 1
    for i in range(11, -1, -1): 
        if totals[i] > size / 2:
            gamma += binary
        else:
            epsilon += binary
        binary = binary * 2
    print(f"gamma: {gamma}")
    print(f"epsilon: {epsilon}")
    return gamma * epsilon


def part_two(the_input):
    saved_list = the_input.copy()
    oxygen_rating = 0
    co2_rating = 0
    for i in range(12):
        total = 0
        most_common = most_common_bit(the_input, i)
        new_input = list()
        for line in the_input:
            if int(line[i]) == most_common:
                new_input.append(line)
        the_input = new_input
        if len(the_input) == 1: 
            print(f"Found {the_input} as winner")
            oxygen_rating = string_to_binary(the_input[0])
            print(f"Found {oxygen_rating} as the decimal")
            break
    the_input = saved_list
    for i in range(12):
        least_common = least_common_bit(the_input, i) 
        new_input = list()
        for line in the_input:
            if int(line[i]) == least_common:
                new_input.append(line)
        the_input = new_input
        if len(the_input) == 1: 
            print(f"Found {the_input} as winner")
            co2_rating = string_to_binary(the_input[0])
            print(f"Found {co2_rating} as the decimal")
            break
    return oxygen_rating*co2_rating

def most_common_bit(binary_list, position):
    total = 0
    for binary_string in binary_list: 
        total += int(binary_string[position])
    if total >= len(binary_list) / 2: 
        return 1
    else:
        return 0

def least_common_bit(binary_list,position): 
    total = 0
    for binary_string in binary_list: 
        total += int(binary_string[position])
    if total >= len(binary_list) / 2: 
        return 0
    else:
        return 1

def string_to_binary(binary_string): 
    binary = 1;
    binary_string = binary_string[::-1]
    total = 0;
    for i in range(len(binary_string)): 
        total += int(binary_string[i]) * binary
        binary *= 2
    return total

    

if __name__ == "__main__":
    the_input = list()
    with open('3.in') as f:
    #with open('3.in') as f:
        for line in f:
            the_input.append(line.rstrip())

    part_one = part_one(the_input)
    part_two = part_two(the_input)
    print(f"Part 1: {part_one}")
    print(f"Part 2: {part_two}")
