from collections import deque
import bisect

class Location:
    def __init__(self, rc, steps, height):
        self.location = rc
        self.steps = steps
        self.height = height

    def __lt__(self, other):
        return self.steps < other.steps

heights = []
with open('python/12.in','r') as f:
    for x in f.readlines():
        heights.append([height for height in x.strip()])

print(heights)

steps = 0
visited = set()
next_locations = deque([])
starting_rc = (0,0)

max_r = len(heights)
max_c = len(heights[0])

for r in range(max_r):
    for c in range(max_c):
        if heights[r][c] == 'E':
            starting_rc = (r,c)
            break

current_location = Location(starting_rc, 0, 'z')

print(current_location.location)

while current_location.height not in ['a', 'S']:

    if current_location.location not in visited:

        visited.add((current_location.location))
        (r,c) = current_location.location

        # try up
        if r > 0:
            next_loc = (r-1, c)
            if heights[r-1][c] >= 'a':
                if ord(current_location.height) - ord(heights[r-1][c]) <= 1:
                    bisect.insort(next_locations, Location(next_loc, current_location.steps + 1, heights[r-1][c]))
            elif heights[r-1][c] == 'E' and current_location.height in ['y', 'z']:
                bisect.insort(next_locations, Location(next_loc, current_location.steps + 1, heights[r-1][c]))

        # try down
        if r < max_r - 1:
            next_loc = (r+1, c)
            if heights[r+1][c] >= 'a':
                if ord(current_location.height) - ord(heights[r+1][c]) <= 1:
                    bisect.insort(next_locations, Location(next_loc, current_location.steps + 1, heights[r+1][c]))
            elif heights[r+1][c] == 'E' and current_location.height in ['y', 'z']:
                bisect.insort(next_locations, Location(next_loc, current_location.steps + 1, heights[r+1][c]))
                

        # try left
        if c > 0:
            next_loc = (r, c-1)
            if heights[r][c-1] >= 'a':
                if ord(current_location.height) - ord(heights[r][c-1]) <= 1:
                    bisect.insort(next_locations, Location(next_loc, current_location.steps + 1, heights[r][c-1]))
            elif heights[r][c-1] == 'E' and current_location.height in ['y', 'z']:
                bisect.insort(next_locations, Location(next_loc, current_location.steps + 1, heights[r][c-1]))
            

        # try right
        if c < max_c - 1:
            next_loc = (r, c+1)
            if heights[r][c+1] >= 'a':
                if ord(current_location.height) - ord(heights[r][c+1]) <= 1:
                    bisect.insort(next_locations, Location(next_loc, current_location.steps + 1, heights[r][c+1]))
            elif heights[r][c+1] == 'E' and current_location.height in ['y', 'z']:
                bisect.insort(next_locations, Location(next_loc, current_location.steps + 1, heights[r][c+1]))
            
    current_location = next_locations.popleft()

print(current_location.steps)


