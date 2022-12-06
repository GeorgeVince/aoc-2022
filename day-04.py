with open("./input/day-04.txt", 'r') as f:
    contents = [x.strip() for x in f.readlines()]

total = 0
for row in contents:
    elf_1, elf_2 = row.split(",")
    e_1_lower, e_1_higher = elf_1.split("-")
    e_2_lower, e_2_higher = elf_2.split("-")

    e_1_lower = int(e_1_lower)
    e_1_higher = int(e_1_higher)
    e_2_lower = int(e_2_lower)
    e_2_higher = int(e_2_higher)

    if e_1_lower >= e_2_lower and e_1_higher <= e_2_higher:
        total +=1
        continue
    if e_1_lower <= e_2_lower and e_1_higher >= e_2_higher:
        total +=1
        continue
print(total)

total = 0
for row in contents:
    print(row, total)
    elf_1, elf_2 = row.split(",")
    e_1_lower, e_1_higher = elf_1.split("-")
    e_2_lower, e_2_higher = elf_2.split("-")

    e_1_lower = int(e_1_lower)
    e_1_higher = int(e_1_higher)
    e_2_lower = int(e_2_lower)
    e_2_higher = int(e_2_higher)

    if e_1_lower <= e_2_lower:
        while e_1_lower <= e_1_higher:
            if e_1_lower >= e_2_lower and e_1_lower <= e_2_higher:
                total += 1
            e_1_lower += 1
        continue
    
    if e_2_lower <= e_1_lower:
        while e_2_lower <= e_2_higher:
            if e_2_lower >= e_1_lower and e_1_lower <= e_1_higher:
                total += 1
            e_2_lower += 1
        continue
    
print(total)