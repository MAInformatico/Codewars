def likes(names):
    result = ''
    if len(names) == 0: result = 'no one likes this'
    elif len(names) == 1: result = names[0] + ' likes this'   
    elif (len(names) > 1 and len(names) < 4):
        for i in range(0, len(names) - 1):
            result = result + names[i] + ", "
        result = result[:-2]
        result = result + " and " + str(names[len(names) - 1]) + " like this"
    else:
        for name in range(0, 2):
            result = result + names[name] + ", "
        result = result[:-2]
        result = result + " and " + str(len(names)-2) + " others like this"
    return result
