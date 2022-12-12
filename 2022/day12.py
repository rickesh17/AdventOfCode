import numpy as np
import collections

data = """Add data here"""

data = [list(x.strip()) for x in data.split("\n")]
elevations = np.array([[ord(char) - ord('a') for char in line] for line in data])
source = tuple(x[0] for x in np.where(elevations == ord('S') - ord('a')))
target = tuple(x[0] for x in np.where(elevations == ord('E') - ord('a')))
elevations[source] = 0
elevations[target] = 26

xmax, ymax = elevations.shape

def grid_neighbors(x, y):
    candidates = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    return [c for c in candidates if 0 <= c[0] < xmax and 0 <= c[1] < ymax]

def find_neighbors(x, y):
    return [n for n in grid_neighbors(x ,y) if elevations[n] - elevations[x, y] <= 1]

def reversed_neighbors(x, y):
    return [n for n in grid_neighbors(x, y) if elevations[x, y] - elevations[n] <= 1]

def navigate(source, neighbor_func, stop_condition):
    active = collections.deque([(source, 0)])
    seen = set()
    while active:
        current, steps = active.popleft()
        if stop_condition(current):
            return steps
        if current in seen:
            continue
        seen.add(current)
        for neighbor in neighbor_func(*current):
            active.append((neighbor, steps + 1))
    return np.inf

navigate(target, reversed_neighbors, lambda x: elevations[x] == 0)