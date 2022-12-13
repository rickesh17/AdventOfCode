data = """Add data here"""

def evaluate(a, b):
    for i in range(len(a)):
        if i >= len(b):
            return 1 

        left = a[i]
        right = b[i]
        if type(left) == int and type(right) == int:
            if left > right:
                return 1
            elif left < right:
                return -1
        elif type(left) == list and type(right) == list:
            result = evaluate(left, right)
            if result != -2:
                return result 
        elif type(left) == int:
            return evaluate([left], right)
        elif type(right) == int:
            return evaluate(left, [right])

    if len(a) == len(b):
        return -2

    return -1


def part_1(data):
    answer = 0
    for i, pairs in enumerate(data.strip().split('\n\n')):
        left, right = map(eval, pairs.split('\n'))
        if evaluate(left, right) == -1:
            answer += (i + 1)
    return answer


def part_2(data):
    d1 = [[2]] 
    d2 = [[6]]
    packets = list(map(eval, filter(None, data.strip().split('\n')))) + [d1, d2]
    packets.sort(key=cmp_to_key(evaluate))
    return (packets.index(d1) + 1) * (packets.index(d2) + 1)