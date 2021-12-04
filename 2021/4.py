#!/usr/bin/boithon
from Board import Board
import re

def part_one(boards, sequence):
    for number in sequence: 
        print(f"Calling {number}")
        for board in boards: 
            if board.call_number(number) == 1: 
                print(f"Found winner with {number}!")
                return board.score_board(number)
    return 0 


def part_two(boards, sequence):
    for number in sequence: 
        print(f"Calling {number}")
        remaining_boards = list()
        for board in boards: 
            if board.call_number(number) == 1: 
                print(f"Found winner with {number}!")
                if len(boards) == 1: 
                    print(f"This is the last board remaining!")
                    return board.score_board(number)
            else:
                remaining_boards.append(board)
        boards = remaining_boards
    return 0 


if __name__ == "__main__":
    boards = list()
    with open('4.in') as f:
        sequence = f.readline().rstrip().split(',')

        board_numbers = list()
        for line in f:
            line = line.strip()
            if not re.match('\d',line):
                continue
            for i in line.split():
                board_numbers.append(i)
            if len(board_numbers) >= 24:
                board = Board(board_numbers)
                boards.append(board)
                board_numbers = list()

    part_one = part_one(boards, sequence)
    for board in boards: 
        board.reset()
    part_two = part_two(boards,sequence)
    print(f"Part 1: {part_one}")
    print(f"Part 2: {part_two}")


