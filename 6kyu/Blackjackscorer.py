def score_hand(cards):
    result = 0 
    ace = 0 
    for i in cards:
        if i == 'A' : ace += 1 ; result += 1 
        elif i in ['K','Q','J'] : result += 10 
        else: 
            result += int(i)
    for i in range(1,ace+1,1):
        if result + 10 <= 21 : result += 10
        else: 
            break
    return result
