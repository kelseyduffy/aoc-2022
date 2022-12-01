import this


elves = []
this_elf = []
with open('python/01.in','r') as f:
    for x in f.readlines():
        if x.isspace():
            elves.append(this_elf)
            this_elf = []
        else:
            this_elf.append(int(x))
    elves.append(this_elf)

# part 1

elf_totals = [sum(elf) for elf in elves]
print(max(elf_totals))

# part 2

elf_totals.sort()
print(sum(elf_totals[-3:]))
