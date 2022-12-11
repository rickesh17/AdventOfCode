import math
from functools import reduce

data = """Add data here"""

def get_monkey_info(data):
    split_data = data.split("\n\n")
    monkey_dict = {}
    for d in split_data:
        monkey = ""
        for sentence in d.split("\n"):
            if "Monkey " in sentence:
                monkey = sentence.replace(":", "").split(" ")[-1]
                monkey_dict[monkey] = {"rule_operator": "",
                                       "rule_num": 0,
                                       "divisor": 0,
                                       "true_send": "",
                                       "false_send": "",
                                       "items": [],
                                       "inspected": 0}
            if "Starting items: " in sentence:
                items = [int(item) for item in sentence.split(": ")[-1].split(", ")]
                monkey_dict[monkey]["items"].extend(items)
            elif "Operation" in sentence:
                a, b, c, d, operator, num = sentence.strip().split(" ")
                if num == "old":
                    operator = "squared"
                    num = 0
                monkey_dict[monkey]["rule_operator"] = operator
                monkey_dict[monkey]["rule_num"] = int(num)
            elif "Test" in sentence:
                divisor = sentence.split(" ")[-1]
                monkey_dict[monkey]["divisor"] = int(divisor)
            elif "If true" in sentence:
                true_monkey = sentence.split(" ")[-1]
                monkey_dict[monkey]["true_send"] = true_monkey
            elif "If false" in sentence:
                false_monkey = sentence.split(" ")[-1]
                monkey_dict[monkey]["false_send"] = false_monkey    
    return monkey_dict

def monkey_inspections(monkey_dict, worry_divider, rounds):
    for i in range(1, rounds + 1):
        for monkey, info in monkey_dict.items():
            items = info["items"]
            for item in items:
                monkey_dict[monkey]["inspected"] += 1
                if info["rule_operator"] == "+":
                    worry_item = math.floor((item + info["rule_num"]) / worry_divider)
                elif info["rule_operator"] == "*":
                    worry_item = math.floor((item * info["rule_num"]) / worry_divider)
                else:
                    worry_item = math.floor((item * item) / worry_divider)
                if worry_item % info["divisor"] == 0:
                    monkey_dict[info["true_send"]]["items"].append(worry_item)
                else:
                    monkey_dict[info["false_send"]]["items"].append(worry_item)
            monkey_dict[monkey]["items"] = []
    return monkey_dict

def solution(data, divider, rounds):
    monkey_dict = get_monkey_info(data)
    monkey_dict = monkey_inspections(monkey_dict, divider, rounds)
    inspected = []
    for k, v in monkey_dict.items():
        inspected.append(v["inspected"])
    return reduce(lambda x, y: x*y, sorted(inspected)[-2:])
