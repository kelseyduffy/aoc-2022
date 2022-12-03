
def priority_score(item_set):
    for item in item_set: # should only be 1, need to unwrap the set
        if 'a' <= item <= 'z':
            return (ord(item) - ord('a') + 1)
        else:
            return (ord(item) - ord('A') + 27)

rucksacks = []
with open('python/03.in','r') as f:
    for x in f.readlines():
        rucksacks.append(x.strip())

# part 1

score = 0

for rucksack in rucksacks:
    compartment1 = {item for item in rucksack[:len(rucksack)//2]}
    compartment2 = {item for item in rucksack[len(rucksack)//2:]}
    score += priority_score(compartment1.intersection(compartment2))      

print(score)

# part 2

score = 0 

for i in range (0,len(rucksacks),3):
    ruckset1 = {item for item in rucksacks[i]}
    ruckset2 = {item for item in rucksacks[i + 1]}
    ruckset3 = {item for item in rucksacks[i + 2]}
    score += priority_score(ruckset1.intersection(ruckset2.intersection(ruckset3)))

print(score)
