def solution(number):
    result = 0
    for i in range(0,number):
        if((i%5==0 and i%3!=0) or (i%5!=0 and i%3==0) or (i%5==0 and i%3==0) ):
            result+=i
    return result
