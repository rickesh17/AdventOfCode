data = """Add data here"""

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def part_1(data, alphabet):
    total = 0
    for d in data.split("\n"):
        length = int(len(d) / 2)
        first = d[:length]
        second = d[length:]
        common = list(set(first).intersection(second))[0]
        priority = alphabet.find(common) + 1
        total += priority
    return total

def part_2(data, alphabet, n):
    total = 0
    split_data = data.split("\n")
    list_of_groups = zip(*(iter(split_data),) * n)
    for first, second, third in list_of_groups:
        common = list(set(first).intersection(second).intersection(third))[0]
        priority = alphabet.find(common) + 1
        total += priority
    return total