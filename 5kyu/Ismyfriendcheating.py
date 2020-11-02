def remov_nb(n):
    total = n*(n+1)/2
    result = []
    for i in range(1,n+1):
        j = (total-i)/(i+1.0)
        if j.is_integer() and j <= n:
            result.append((i,int(j)))
    return result
