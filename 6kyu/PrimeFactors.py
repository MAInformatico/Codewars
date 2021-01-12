def prime_factors(n):
    i = 2
    factors = {}
    while n/i != 1:
      if n%i == 0:
        if i in factors:
            factors[i] = factors[i]+1
        else:
            factors[i] = 1
        n = n/i
      else:
        i+=1

    if i in factors:
        factors[i] = factors[i]+1
    else:
        factors[i] = 1
    result = ''
    factors = sorted(factors.items(),key = lambda x:x[0])

    for key in factors:
        if key[1] == 1:
           result = result + '('+str(key[0]) +')'
        else:
           result = result + '(' +str(key[0]) + '**' + str(key[1]) + ')'
    return result
