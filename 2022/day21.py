data = """Add data here"""

def iterate(job_dict, not_complete):
    still_not_complete = []
    for x in not_complete:
        split_x = x.split(" ")
        k = split_x[0]
        split_v = split_x[1:]
        if len(split_v) == 1:
            job_dict[k] = split_v[0]
        else:
            first, operator, second = split_v
            if first in job_dict and second in job_dict:
                if "?" not in job_dict[first] and "?" not in job_dict[second]:
                    job_dict[k] = str(eval("".join([job_dict[first], operator, job_dict[second]])))
                else:
                    job_dict[k] = "".join([job_dict[first], operator, job_dict[second]])
            else:
                still_not_complete.append(" ".join([k] + split_v))
    return job_dict, still_not_complete

def part_1(data):
    job_dict = {}
    not_complete = []
    for d in data.split("\n"):
        k, v = d.split(": ")
        split_v = v.split(" ")
        not_complete.append(" ".join([k] + split_v))
    
    while not_complete:
        job_dict, not_complete = iterate(job_dict, not_complete)
    return job_dict["root"]

def part_2(data):
    job_dict = {}
    not_complete = []
    for d in data.split("\n"):
        k, v = d.split(": ")
        if k == "root":
            v = v.replace("+", "=")
        if k == "humn":
            v = "?"
        split_v = v.split(" ")
        if k == "root":
            e1, o, e2 = split_v
        not_complete.append(" ".join([k] + split_v))
    
    while e1 not in job_dict or e2 not in job_dict:
        job_dict, not_complete = iterate(job_dict, not_complete)
        
    return eval(job_dict[e1].replace("?", job_dict[e2]))