head_moves = []
with open('python/09.in','r') as f:
    for x in f.readlines():
        head_moves.append(x.strip())

knot_counts = [2,10]

for knot_count in knot_counts:

    tail_positions = set()
    knots = []

    for _ in range(knot_count):
        knots.append([0,0])
    tail_positions.add((knots[-1][0], knots[-1][1]))

    for move in head_moves:
        (dir, count) = move.split(' ')
        for i in range(int(count)):
            if dir == 'U':
                knots[0][1] += 1
            elif dir == 'D':
                knots[0][1] -= 1
            elif dir == 'R':
                knots[0][0] += 1
            else:
                knots[0][0] -= 1

            for i in range(1,knot_count):
            
                if not (abs(knots[i][0] - knots[i-1][0]) >= 2 or abs(knots[i][1] - knots[i-1][1]) >= 2):
                    # no movement
                    continue

                if knots[i][0] > knots[i-1][0]:
                    knots[i][0] -= 1
                
                if knots[i][0] < knots[i-1][0]:
                    knots[i][0] += 1
                
                if knots[i][1] > knots[i-1][1]:
                    knots[i][1] -= 1

                if knots[i][1] < knots[i-1][1]:
                    knots[i][1] += 1
            
            tail_positions.add((knots[-1][0],knots[-1][1]))

    print(len(tail_positions))
