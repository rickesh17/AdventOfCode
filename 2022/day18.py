import numpy as np
import scipy.ndimage as ndi

data = """Add data here"""

A = np.zeros((25,25,25), int)

for x in map(eval, data.split("\n")): A[x] = 1
A = np.pad(A, 1)

w = np.zeros((3,3,3))
w[0,1,1]=1; w[2,1,1]=1
w[1,0,1]=1; w[1,2,1]=1
w[1,1,0]=1; w[1,1,2]=1

edges = lambda A: (ndi.convolve(A, w) * (1-A)).sum()

part1 = edges(A)
part2 = part1 - edges(ndi.binary_fill_holes(A) - A)

print(part1, part2)