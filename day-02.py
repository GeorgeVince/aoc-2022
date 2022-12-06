from re import X


with open("./input/day-02.txt", 'r') as f:
    contents = [x.strip() for x in f.readlines()]

ROCK = 'X'
PAPER = 'Y'
SCISSORS = 'Z'

THEM_ROCK = 'A'
THEM_PAPER = 'B'
THEM_SCISSORS = 'C'

US_WIN_LOOSE = {ROCK:THEM_SCISSORS, PAPER:THEM_ROCK, SCISSORS:THEM_PAPER}
THEM_WIN_LOOSE = {THEM_ROCK:SCISSORS, THEM_PAPER:ROCK, THEM_SCISSORS:PAPER}

WIN=6
DRAW=3
LOOSE=0

total = 0
for row in contents:
    them, us = row.split(" ")
    total += list(US_WIN_LOOSE.keys()).index(us) + 1
    if US_WIN_LOOSE.get(us) == them:
        total += WIN
    elif THEM_WIN_LOOSE.get(them) == us:
        total += LOOSE
    else:
        total += DRAW
print(f"Part 1: {total}")
    



