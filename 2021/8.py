#!/usr/bin/boithon

#Generates statistics on a number that we can use to identify what it is
def generate_stats(number_display): 
    #Mappings are numbers within other numbers, for example: to display the number 8, 1 is always displayed within it
    mappings = list()
    for wanted_number,wanted_display in number_display.items(): 
        for number,display in number_display.items(): 
            found = 1
            if number == wanted_number:
                continue
            for letter in wanted_display:
                if letter not in display: 
                    found = 0
            if found == 1: #We found a mapping
                mappings.append((wanted_number,number))

    #Lets generate some profiles for every number
    number_stats = {}
    for number,display in number_display.items(): 
        length = len(number_display[number])
        display = number_display[number]
        contained_in = list()
        contains_number = list()
        for i,j in mappings: 
            if i == number:
                contained_in.append(j)
            if j == number: 
                contains_number.append(i)
        
        number_stats[number] = { 
            'display': display,
            'display_length': length,
            'contained_in': contained_in,
            'contained_in_length': len(contained_in),
            'contains_number': contains_number,
            'contains_number_length': len(contains_number)
        }
    return number_stats

#Given the stats of a good display, we can compare a bad display to it and get it working
def fix_display(good_display_stats,bad_display): 
    stats = generate_stats(bad_display) 
    fixed_display = dict()
    for number,stats in stats.items(): 
        for good_number,good_stats in good_display_stats.items(): 
            match = 1
            for stat in ('display_length','contained_in_length','contains_number_length'): 
                if stats[stat] != good_stats[stat]:
                    match = 0
            if match == 1: 
                fixed_display[good_number] = stats['display']
                continue
    return fixed_display


def decode_output(number_stats): 
    output_values = list()
    with open('8.in') as f:
        for line in f:
            #Parse and process the display
            display = dict()
            display_blob,output_blob = line.split('|')
            i = 0
            for d in display_blob.split(): 
                display[i] = sort_string(d)
                i += 1
            display = fix_display(number_stats,display)

            #Parse and process output
            number = ""
            for output in output_blob.split(): 
                output = sort_string(output)
                for item,value in display.items(): 
                    if output == value: 
                        number += str(item)
                        continue
            output_values.append(int(number))

    return output_values

def sort_string(string): 
    sorted_string = sorted(string)
    return "".join(sorted_string)

def part_one(output):
    total = 0
    for line in output: 
        line = str(line)
        total += line.count('1') + line.count('4') + line.count('7') + line.count('8')                
    return total


def part_two(output): 
    return sum(output)


if __name__ == "__main__":

    #Generate statistics on our working display
    number_display = {
        1: 'cf',
        2: 'acdeg',
        3: 'acdfg',
        4: 'bcdf',
        5: 'abdfg',
        6: 'abdefg',
        7: 'acf',
        8: 'abcdefg',
        9: 'abcdfg',
        0: 'abcefg'
    }
    number_stats = generate_stats(number_display)
    output = decode_output(number_stats)
    
    answer_part_one = part_one(output)
    print(f"Part one:\n{answer_part_one}") 
    answer_part_two = part_two(output)
    print(f"Part two:\n{answer_part_two}") 
