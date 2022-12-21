data = """Add data here"""

def get_stacks(stacks):
    split_stacks = stacks.split("\n")[:-1]
    column_numbers = stacks.split("\n")[-1:][0]
    
    columns = {}
    for num in column_numbers.split():
        columns[num] = []
        
    for layer in split_stacks:
        l = layer.replace("    ", " x ").split()
        for i, item in enumerate(l, 1):
            if item != "x":
                columns[str(i)].insert(0, item)
    return columns

def part_1(columns, instructions):
    for instruction in instructions.split("\n"):
        m, f, t = instruction.replace("move ", "").replace("from ", "").replace("to ", "").split(" ")
        for i in range(1, int(m) + 1):
            transfer = columns[f][-1:][0]
            del columns[f][-1]
            columns[t].append(transfer)
    return columns

def part_2(columns, instructions):
    for instruction in instructions.split("\n"):
        m, f, t = instruction.replace("move ", "").replace("from ", "").replace("to ", "").split(" ")
        transfer = columns[f][-int(m):]
        for i in range(1, int(m) + 1):
            del columns[f][-1]
        columns[t].extend(transfer)  
    return columns

def solution(data, part):
    stacks, instructions = data.split("\n\n")
    columns = get_stacks(stacks)
    final_columns = part(columns, instructions)
    final_items = ""
    for k, v in columns.items():
        if len(v) > 0:
            final_items += v[-1][1]
    return final_items
