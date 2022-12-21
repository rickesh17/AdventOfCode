data = """Add data here with '\n' seperators between elves"""

def part_1(data):
    food_dict = {}
    for i, d in enumerate(data.split("\n\n")):
        food_dict[i + 1] = sum([int(item) for item in list(filter(None, d.split("\n")))])
    return food_dict[max(food_dict, key=food_dict.get)]

def part_2(data):
    food_dict = {}
    for i, d in enumerate(data.split("\n\n")):
        food_dict[i + 1] = sum([int(item) for item in list(filter(None, d.split("\n")))])
    return sum(list(dict(sorted(food_dict.items(), key=lambda item: item[1])).values())[-3:])

