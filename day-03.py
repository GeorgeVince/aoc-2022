with open("./input/day-03.txt", 'r') as f:
    contents = [x.strip() for x in f.readlines()]

def calculate_score(letter: str) -> int:
    if letter.islower():
            return ord(letter) - 96
    if letter.isupper():
            return ord(letter) - 64 + 26

total = 0
for rucksack in contents:
    first, second = rucksack[:len(rucksack) // 2], rucksack[len(rucksack)//2:]
    letter = list(set(first).intersection(second))[0]
    total += calculate_score(letter)
print(total)

total = 0
groups = []
for indx, rucksack in enumerate(contents):
    groups.append(rucksack)
    if (indx + 1) % 3 == 0 and indx > 0:
        first, second, third = groups
        common = list(set(first).intersection(second, third))[0]
        total += calculate_score(common)
        groups = []
print(total)