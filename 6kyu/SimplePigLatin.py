def pig_it(text):
    alpha = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ0123456789"
    text = text.split(" ")
    result = []
    
    for i in range(len(text)):
        if text[i] in alpha and len(text[i]) == 1:
            text[i] = text[i]+ "ay"
            
        elif len(text[i]) >= 2:
            text[i] = text[i][1: -1]+ text[i][-1]+  text[i][0]+ "ay"
        
        else: text[i] = text[i]
        result.append(text[i])
        
    return " ".join(result)
