elf_pairs = []
with open('python/04.in','r') as f:
    for x in f.readlines():
        elf_pairs.append(x.strip().split(','))

# part 1

overlaps = 0

for elf_pair in elf_pairs:
    elf1 = elf_pair[0].split('-')
    elf2 = elf_pair[1].split('-')

    if elf1[0] == elf2[0] and elf1[1] == elf2[1]:
        overlaps += 1
        continue

    if int(elf1[0]) >= int(elf2[0]):
        if int(elf1[1]) <= int(elf2[1]):
            overlaps += 1
            continue

    if int(elf1[0]) <= int(elf2[0]):
        if int(elf1[1]) >= int(elf2[1]):
            overlaps += 1
            continue

print(overlaps)

# part 2

overlaps = 0

for elf_pair in elf_pairs:
    elf1 = elf_pair[0].split('-')
    elf2 = elf_pair[1].split('-')

    if not (int(elf1[0]) > int(elf2[1]) or int(elf2[0]) > int(elf1[1])):
        overlaps += 1

print(overlaps)