ops = []
with open('python/10.in','r') as f:
    for x in f.readlines():
        ops.append(x.strip())

checkpoints = [20, 60, 100, 140, 180, 220] 
total_strengths = 0

signal_strength = 1
cycle = 0

for op in ops:
    signal_at_start = signal_strength
    instruction = op.split(' ')

    if instruction[0] == 'noop':
        cycle += 1

    else:
        cycle += 2
        signal_strength += int(instruction[1])
    
    for i in range(len(checkpoints)):
        if checkpoints[i] > -1:
            if cycle >= checkpoints[i]:
                total_strengths += (signal_at_start * checkpoints[i])
                checkpoints[i] = -1

print(total_strengths)
