data = """Add data here"""

def solution(data, l):
    start = 0
    for i in range(len(data)):
        substring = data[i:i + l]
        if len(set(substring)) == l:
            start = i + l
            break
    return start