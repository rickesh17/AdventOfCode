data = """Add data here"""

def part_1(data):
    trees = np.array([list(line.strip()) for line in data.split("\n")], int)
    total = trees.shape[0] * trees.shape[1]
    for hor in range(1,trees.shape[0]-1):
        for vert in range(1,trees.shape[1]-1):
            h = trees[hor,vert]
            if h <= np.max(trees[hor+1:,vert]) and h <= np.max(trees[:hor,vert]) and h <= np.max(trees[hor,vert+1:]) and h <= np.max(trees[hor,:vert]):
                total -= 1
    return total

def part_2(data):
    trees = np.array([list(line.strip()) for line in data.split("\n")], int)
    max_scenic = 0
    for hor in range(1,trees.shape[0]-1):
        for vert in range(1,trees.shape[1]-1):
            h = trees[hor,vert]
            for i in range(1,hor+1):
                if trees[hor-i,vert] >= h: break
            scenic = i
            for i in range(1,trees.shape[0]-hor):
                if trees[hor+i,vert] >= h: break
            scenic *= i
            for j in range(1,vert+1):
                if trees[hor,vert-j] >= h: break
            scenic *= j
            for j in range(1,trees.shape[1]-vert):
                if trees[hor,vert+j] >= h: break
            scenic *= j
            if scenic > max_scenic:
                max_scenic = scenic
    return max_scenic
