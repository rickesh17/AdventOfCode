data = """Add data here"""

def part_1(data):
    fully_contains = 0
    for d in data.split("\n"):
        first, second = d.split(",")
        fbeg, fend = first.split("-")
        sbeg, send = second.split("-")
        first_areas = list(range(int(fbeg), int(fend) + 1))
        second_areas = list(range(int(sbeg), int(send) + 1))
        if set(first_areas) <= set(second_areas) or set(second_areas) <= set(first_areas):
            fully_contains += 1
    return fully_contains

def part_2(data):
    fully_contains = 0
    for d in data.split("\n"):
        first, second = d.split(",")
        fbeg, fend = first.split("-")
        sbeg, send = second.split("-")
        first_areas = list(range(int(fbeg), int(fend) + 1))
        second_areas = list(range(int(sbeg), int(send) + 1))
        if set(first_areas).intersection(set(second_areas)) or set(second_areas).intersection(set(first_areas)):
            fully_contains += 1
    return fully_contains