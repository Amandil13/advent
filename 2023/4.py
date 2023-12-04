#!/usr/bin/boithon
from collections import namedtuple,defaultdict
import re


def import_data():
    with open('4.in') as f:
        data = [line.rstrip() for line in f]
    return data

def part_one(winners,picks):
    total = 0
    for key,value in winners.items(): 
        cardscore = 0
        for win in value: 
            pick_values =  picks[key]
            try: 
                picks[key].index(win)
                #print(f"key: {key}, value: {win} is a hit in {pick_values}")
                if cardscore == 0: 
                    cardscore = 1
                else: 
                    cardscore *= 2
                print(f"cardscore: {cardscore}")
            except ValueError: 
                pass
        total += cardscore
    return total

def part_two(winners,picks):
    cardcounts = defaultdict(lambda: 1)
    for key,value in winners.items(): 
        cardscore = 0
        for win in value: 
            pick_values =  picks[key]
            try: 
                picks[key].index(win)
                #print(f"key: {key}, value: {win} is a hit in {pick_values}")
                cardscore += 1
            except ValueError: 
                pass
        for i in (range(key + 1,key + cardscore + 1)): 
            print(f"{cardcounts[key]} copies of {key} with {cardscore} matches added to {i}")
            cardcounts[i] += cardcounts[key] 
        print(f"{key}: {cardcounts[key]}")

    return sum(cardcounts.values())

if __name__ == "__main__":
    data = import_data()
    winners = {}
    picks = {}
    i = 1
    for line in data: 
        ar = line.split('|')
        winners[i] = ar[0].split()
        picks[i] = ar[1].split()
        i += 1
    part_one = part_one(winners,picks)
    part_two = part_two(winners,picks)
    print(f"Part 1:\n{part_one}")
    print(f"Part 2:\n{part_two}")
