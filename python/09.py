head_moves = []
with open('python/09.in','r') as f:
    for x in f.readlines():
        head_moves.append(x.strip())

tail_positions = set()

start = [0,0]
head = [0,0]
tail = [0,0]
tail_positions.add((tail[0], tail[1]))

for move in head_moves:
    (dir, count) = move.split(' ')
    for i in range(int(count)):
        if dir == 'U':
            head[1] += 1
        elif dir == 'D':
            head[1] -= 1
        elif dir == 'R':
            head[0] += 1
        else:
            head[0] -= 1
        
        if not (abs(tail[0] - head[0]) >= 2 or abs(tail[1] - head[1]) >= 2):
            # no movement
            continue

        if tail[0] > head[0]:
            tail[0] -= 1
        
        if tail[0] < head[0]:
            tail[0] += 1
        
        if tail[1] > head[1]:
            tail[1] -= 1

        if tail[1] < head[1]:
            tail[1] += 1
        
        tail_positions.add((tail[0],tail[1]))

print(len(tail_positions))
