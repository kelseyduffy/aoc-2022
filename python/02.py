games = []
with open('python/02.in','r') as f:
    for x in f.readlines():
        games.append(x.strip().split(' '))

# part 1

# A/X = Rock
# B/Y = Paper
# C/Z = Scissors

score = 0

for game in games:
    if game[1] == 'X':
        score += 1
        if game[0] == 'A':
            score += 3
        elif game[0] == 'B':
            score += 0
        else: #game[0] == 'C'
            score += 6
    elif game[1] == 'Y':
        score += 2
        if game[0] == 'A':
            score += 6
        elif game[0] == 'B':
            score += 3
        else: #game[0] == 'C'
            score += 0
    else: # game[1] == 'Z'
        score += 3
        if game[0] == 'A':
            score += 0
        elif game[0] == 'B':
            score += 6
        else: #game[0] == 'C'
            score += 3

print(score)

# part 2

# A = Rock
# B = Paper 
# C = Scissors
# X = Loss
# Y = Draw
# Z = Win

score = 0

for game in games:
    if game[1] == 'X':
        score += 0
        if game[0] == 'A':
            score += 3
        elif game[0] == 'B':
            score += 1
        else: # game[0] == 'C'
            score += 2

    elif game[1] == 'Y':
        score += 3
        if game[0] == 'A':
            score += 1
        elif game[0] == 'B':
            score += 2
        else: # game[0] == 'C'
            score += 3

    else: #game[1] == 'Z'
        score += 6
        if game[0] == 'A':
            score += 2
        elif game[0] == 'B':
            score += 3
        else: # game[0] == 'C'
            score += 1

print(score)