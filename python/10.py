def print_image(pixels):
    for i in range(6):
        row = ''
        for j in range(40):
            if pixels[i*40 + j] == 0:
                row += ' '
            else:
                row += '#'
        print(row)

ops = []
with open('python/10.in','r') as f:
    for x in f.readlines():
        ops.append(x.strip())

# part 1

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

# part 2

pixels = [0 for _ in range(240)]

sprite_midpoint = 1
cycle = 0

for op in ops:
    instruction = op.split(' ')

    if instruction[0] == 'noop':
        if abs(sprite_midpoint - (cycle % 40)) < 2:
            pixels[cycle] = 1
        cycle += 1
    
    else:
        if abs(sprite_midpoint - (cycle % 40)) < 2:
            pixels[cycle] = 1
        cycle += 1
        if abs(sprite_midpoint - (cycle % 40)) < 2:
            pixels[cycle] = 1
        cycle += 1
        sprite_midpoint += int(instruction[1])

print_image(pixels)