from dataclasses import dataclass

with open("./input/day-04.txt", "r") as f:
    contents = [x.strip() for x in f.readlines()]


@dataclass
class Elf:
    lower: int
    upper: int
    
    def __post_init__(self):
        self.lower = int(self.lower)
        self.upper = int(self.upper)

pairs = []
for row in contents:
    elf_1, elf_2 = row.split(",")
    pairs.append([Elf(*elf_1.split("-")), Elf(*elf_2.split("-"))])

total = 0
for row in pairs:
    if row[0].lower >= row[1].lower and row[0].upper <= row[1].upper:
        total += 1
        continue
    if row[0].lower <= row[1].lower and row[0].upper >= row[1].upper:
        total += 1
        continue
print(total)

total = 0
for row in pairs:
    if row[0].lower <= row[1].lower:
        while row[0].lower <= row[0].upper:
            if row[0].lower >= row[1].lower and row[0].lower <= row[1].upper:
                total += 1
                break
            row[0].lower += 1
        continue

    if row[1].lower <= row[1].lower:
        while row[1].lower <= row[1].upper:
            if row[1].lower >= row[0].lower and row[1].lower <= row[0].upper:
                total += 1
                break
            row[1].lower += 1
print(total)
