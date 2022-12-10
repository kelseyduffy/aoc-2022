trees = []
with open('python/08.in','r') as f:
    for x in f.readlines():
        trees.append([int(tree) for tree in x.strip()])

visible_trees = 2 * (len(trees) + len(trees[0]) - 2)

for r in range(1, len(trees)-1):
    for c in range(1, len(trees[r])-1):
        
        # tallest to the left
        if trees[r][c] > max(trees[r][:c]):
            visible_trees += 1
            continue
        
        # tallest to the right
        if trees[r][c] > max(trees[r][c+1:]):
            visible_trees += 1
            continue
        
        # tallest up
        visible_up = True
        for t_r in range(r):
            if trees[t_r][c] >= trees[r][c]:
                visible_up = False
                break

        if visible_up:
            visible_trees += 1
            continue

        visible_down = True
        for t_r in range(r+1,len(trees)):
            if trees[t_r][c] >= trees[r][c]:
                visible_down = False
                break
        
        visible_trees += visible_down

print(visible_trees)

best_scenic_score = 0

# ignore edges, their scenic scores are 0
for r in range(1, len(trees)-1):
    for c in range(1, len(trees[r])-1):
        #up
        scenic_up = 0
        for t_r in range(r-1, -1, -1):
            scenic_up += 1
            if trees[t_r][c] >= trees[r][c]:
                break

        #down
        scenic_down = 0
        for t_r in range(r+1, len(trees)):
            scenic_down += 1
            if trees[t_r][c] >= trees[r][c]:
                break
            
        #right
        scenic_right = 0
        for t_c in range(c+1, len(trees[r])):
            scenic_right += 1
            if trees[r][t_c] >= trees[r][c]:
                break
            
        #left
        scenic_left = 0
        for t_c in range(c-1, -1, -1):
            scenic_left += 1
            if trees[r][t_c] >= trees[r][c]:
                break
            
        scenic_score = scenic_up * scenic_down * scenic_left * scenic_right
        best_scenic_score = max(best_scenic_score, scenic_score)

print(best_scenic_score)