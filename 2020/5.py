#!/usr/bin/env python3
import re
import sys

takenseats = []
maxid = 0 
with open('5.in') as f:
    for line in f:

        #Find the row we are on 
        row = line[0:7]
        bottom = 0
        top = 127
        for i in range(7):
            interval = (top - bottom + 1) / 2
            if row[i] == 'F': 
                top -= interval
            else: 
                bottom += interval
        row = bottom

        #let's do the column now
        column = line[7:10]
        bottom = 0
        top = 7
        for i in range(3):
            interval = (top - bottom + 1) / 2
            if column[i] == 'L': 
                top -= interval
            else: 
                bottom += interval
        column = bottom
        
        #Calculate some ids
        seatid = int(8 * row + column)
        maxid = seatid if seatid > maxid else maxid
        takenseats.append(seatid)
        
print("Part one (Max ID):")
print(f"{maxid}")

#Find our seat
for i in range(1, maxid):
    if i in takenseats: 
        continue
    if (i - 1) in takenseats and (i + 1) in takenseats:
        #This is our seat
        print("Part two (Our Seat ID):")
        print(f"Our seat is: {i}")
        break
