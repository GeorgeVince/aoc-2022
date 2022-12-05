with open("./input/day-01.txt", 'r') as f:
    contents = [x.strip() for x in f.readlines()]

totals =[]
subtotal = 0
for row in contents:
    if row == "":
        totals.append(subtotal)
        subtotal = 0
        continue

    subtotal += int(row)

print(f"Part 1: {max(totals)}")

top_three = sum(sorted(totals)[-3:])
print(f"Part 2: {top_three}")
