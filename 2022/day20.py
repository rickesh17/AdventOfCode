data = """Add data here"""

def find(original, shuffle, y, z):
    for a in range(z):
        for x in original:
            if x[1] == 0:
                zero = x
            i = shuffle.index(x)
            shuffle.pop(i)
            shuffle.insert((i + x[1]) % y, x)
    zero = shuffle.index(zero)
    return sum(shuffle[zero + (x * 1000)][1] for x in [1, 2, 3])

def part_1(data):
    enum_data = list(enumerate(int(x) for x in data.split("\n")))
    return find(enum_data, enum_data[:], len(enum_data) - 1, 1)

def part_2(data):
    enum_data = list(enumerate(int(x) for x in data.split("\n")))
    enum_data = [(x[0], x[1] * 811589153) for x in enum_data]
    return find(enum_data, enum_data[:], len(enum_data) - 1, 10)