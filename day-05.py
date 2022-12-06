from dataclasses import dataclass, field
from typing import List, Tuple
from collections import defaultdict
import re


@dataclass
class CargoStack:
    stack: List[str] = field(default_factory=list) 

@dataclass
class Instruction:
    move: int
    _from: int
    to: int

    def __post_init__(self):
        self.move = int(self.move)
        self._from = int(self._from)
        self.to = int(self.to)

def parse_input() -> Tuple[List[CargoStack], List[Instruction]]:
    with open("./input/day-05.txt", "r") as f:
        contents = [x for x in f.readlines()]

    stacks = defaultdict(CargoStack)
    instructions = []
    for line in contents:
        for indx, char in enumerate(line):
            if char == "[":
                # Get the next char
                letter = line[indx + 1]
                # Work out the stack
                stack_pos = (indx / 4) + 1
                stacks[stack_pos].stack.append(letter)
        
        if 'move' in line:
            instructions.append(Instruction(*re.findall('\d+', line )))
    
    return stacks, instructions


stacks, instructions = parse_input()
print(stacks)
for instruction in instructions:
    
    # Pick stuff up!
    to_move = []
    while instruction.move:
        to_move.append(stacks[instruction._from].stack.pop(0))
        instruction.move -= 1

    to_move.reverse()

    # Place is back down!
    stacks[instruction.to].stack = to_move + stacks[instruction.to].stack 
    print(stacks)

top_letters = []
for key in sorted(stacks.keys()):
    top_letters.append(stacks[key].stack[0])

print("".join(top_letters))

stacks, instructions = parse_input()
print(stacks)
for instruction in instructions:
    
    # Pick stuff up!
    to_move = []
    while instruction.move:
        to_move.append(stacks[instruction._from].stack.pop(0))
        instruction.move -= 1

    # Place is back down!
    stacks[instruction.to].stack = to_move + stacks[instruction.to].stack 
    print(stacks)

top_letters = []
for key in sorted(stacks.keys()):
    top_letters.append(stacks[key].stack[0])

print("".join(top_letters))