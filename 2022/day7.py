data = """Add data here"""

def get_chunks(data):
    split_data = data.split("\n")
    chunks = []
    subchunk = []
    for d in split_data:
        if "$ cd" in d:
            chunks.append(subchunk)
            subchunk = [d]
        else:
            subchunk.append(d)
        if d == split_data[-1]:
            chunks.append(subchunk)
    chunks = chunks[1:]
    return chunks

def get_data_tree(chunks):
    data_tree = {}
    directory = ""
    parent_key = ""
    lvl = 0
    previous_keys = []
    for chunk in chunks:
        for c in chunk:
            if "$ cd" in c:
                directory = c.split(" ")[-1]
                if directory != "..":
                    k = "{}-{}".format(directory, lvl)
                    directory_key = "{}/{}".format("/".join(previous_keys), k)
                    data_tree[directory_key] = {"lvl": lvl,
                                                "total": 0,
                                                "children": []}
                    lvl += 1
                    previous_keys.append(k)
                else:
                    lvl -= 1
                    del previous_keys[-1]
            elif "$ ls" in c:
                continue
            elif "dir" in c:
                sub_d = c.split(" ")[-1]
                sub_d_key = "{}/{}-{}".format(directory_key, sub_d, lvl)
                if lvl == 1:
                    sub_d_key = sub_d_key[1:]
                data_tree[directory_key]["children"].append(sub_d_key)
            else:
                size = c.split(" ")[0]
                data_tree[directory_key]["total"] += int(size)
        parent_key = directory_key
    
    max_lvl = 0
    for k, v in data_tree.items():
        if v['lvl'] > max_lvl:
            max_lvl = v["lvl"]
    max_lvl
    
    for i in reversed(range(0, max_lvl)):
        filtered_dict = {k: v for k, v in data_tree.items() if v['lvl'] == i}
        for k, v in filtered_dict.items():
            children = v["children"]
            for c in children:
                v['total'] += data_tree[c]['total']
    
    return data_tree

def part_1(data):
    chunks = get_chunks(data)
    data_tree = get_data_tree(chunks)
    
    total = 0
    for k, v in data_tree.items():
        v_total = v['total']
        if v_total < 100000:
            total += v_total
    return total

def part_2(data):
    chunks = get_chunks(data)
    data_tree = get_data_tree(chunks)
    max_space = 70000000
    space_used = [v["total"] for k, v in data_tree.items() if v["lvl"] == 0][0]
    unused_space = max_space - space_used
    space_needed = 30000000 - unused_space
    deleted_size = min([v["total"] for k, v in data_tree.items() if v["total"] > space_needed])
    return deleted_size
