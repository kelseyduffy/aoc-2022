crate_strings = []

crate_strings.append('') # everything is 1 indexed
crate_strings.append('WDGBHRV')
crate_strings.append('JNGCRF')
crate_strings.append('LSFHDNJ')
crate_strings.append('JDSV')
crate_strings.append('SHDRQWNV')
crate_strings.append('PGHCM')
crate_strings.append('FJBGLZHC')
crate_strings.append('SJR')
crate_strings.append('LGSRBNVM')

crate_stacks = [[crate for crate in crate_string] for crate_string in crate_strings]

#print(crate_stacks)

operations = []
ops_started = False

with open('python/05.in','r') as f:
    for x in f.readlines():
        if ops_started:
            operations.append(x.strip())
        else:
            if x == '\n':
                ops_started = True

#print(operations)

# part 1

for operation in operations:
    _, number, _, source, _, dest = operation.split(' ')
    
    for _ in range(int(number)):
        crate = crate_stacks[int(source)].pop()
        crate_stacks[int(dest)].append(crate)

for crate_stack in crate_stacks:
    print(crate_stack[-1:])

# part 2

crate_stacks = [[crate for crate in crate_string] for crate_string in crate_strings]

for operation in operations:
    _, number, _, source, _, dest = operation.split(' ')
    
    temp_stack = []
    for _ in range(int(number)):
        crate = crate_stacks[int(source)].pop()
        temp_stack.append(crate)
    
    for i in range(len(temp_stack)-1,-1,-1):
        crate_stacks[int(dest)].append(temp_stack[i])

for crate_stack in crate_stacks:
    print(crate_stack[-1:])