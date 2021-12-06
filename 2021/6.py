#!/usr/bin/boithon

def procreate_fish(fishes,days): 
    for day in range(days): 
        momma_fishes = 0
        for i in range(9):
            if i == 0: 
                momma_fishes = fishes[0]
            else: 
                fishes[i-1] = fishes[i]
        fishes[8] = momma_fishes
        fishes[6] += momma_fishes
    return sum(fishes)

if __name__ == "__main__":
    #index is the day numbe of the fish, value is number of fishes on that day
    fishes = [0,0,0,0,0,0,0,0,0]
    with open('6.in') as f:
        line = f.read()
        for i in line.rstrip().split(','):
            fishes[int(i)] += 1

    part_one = procreate_fish(fishes.copy(),80)
    part_two = procreate_fish(fishes.copy(),256)
    print(f"Part 1:\n{part_one}")
    print(f"Part 2:\n{part_two}")
