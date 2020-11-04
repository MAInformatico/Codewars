def solution(array_a, array_b):
    result = 0  
    for i in range(len(array_a)):
        diference = abs(array_a[i] - array_b[i])
        result  += diference** 2  
    return result / len(array_a)
