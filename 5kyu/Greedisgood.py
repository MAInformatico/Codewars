from collections import Counter

def score(dice):    
    values = {1:1000, 6:600, 5:500, 4:400, 3:300, 2:200}
    dices = Counter(dice)
    result = 0

    for i,j in dices.items():
        if j >= 3:
            result += values[i] * (j // 3)
        if i == 1:
            result += 100 * (j % 3)
        elif i == 5:
            result += 50 * (j % 3)

    return result
