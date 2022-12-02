import pandas as pd

data = """Add data here"""

score_dict = {"Rock": 1,
              "Paper": 2,
              "Scissors": 3}

letters_dict = {"A": "Rock",
                "B": "Paper",
                "C": "Scissors",
                "X": "Rock",
                "Y": "Paper",
                "Z": "Scissors"}

letters_dict_2 = {"A": "Rock",
                  "B": "Paper",
                  "C": "Scissors",
                  "X": "Lose",
                  "Y": "Draw",
                  "Z": "Win"}

def score(row):
    return score_dict[row]

def result(opp, you):
    if opp == you:
        return 3
    elif (you == "Rock" and opp == "Scissors") or (you == "Scissors" and opp == "Paper") or (you == "Paper" and opp == "Rock"):
        return 6
    else:
        return 0
    
def result_score(opp, result):
    score = 0
    if result == "Draw":
        score += 3
        score += score_dict[opp]
        return score
    elif result == "Win":
        score += 6
        if opp == "Rock":
            score += score_dict["Paper"]
        elif opp == "Paper":
            score += score_dict["Scissors"]
        else:
            score += score_dict["Rock"]
        return score
    else:
        score += 0
        if opp == "Rock":
            score += score_dict["Scissors"]
        elif opp == "Paper":
            score += score_dict["Rock"]
        else:
            score += score_dict["Paper"]
        return score
    
def part_1(data):
    df = pd.DataFrame([d.split(" ") for d in data.split("\n")], columns=["Opp", "You"]).replace(letters_dict)
    df['Chosen Score'] = df.apply(lambda row: score(row["You"]), axis=1)
    df['Result Score'] = df.apply(lambda row: result(row["Opp"], row["You"]), axis=1)
    df['Total Score'] = df['Chosen Score'] + df['Result Score']
    total = df['Total Score'].sum()
    return total

def part_2(data):
    df = pd.DataFrame([d.split(" ") for d in data.split("\n")], columns=["Opp", "Result"]).replace(letters_dict_2)
    df['Score'] = df.apply(lambda row: result_score(row["Opp"], row["Result"]), axis=1)
    total = df['Score'].sum()
    return total