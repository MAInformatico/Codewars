import math
def who_is_next(names, r):    
    n = len(names)
    while r > n:
        r = (r - n + 1) >> 1
    return names[r - 1]
