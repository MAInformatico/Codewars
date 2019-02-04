def fusc(n):
    if n <= 1:
        return n
    while n > 2 and n % 2 == 0:
        n /= 2

    return fusc((n - 1) / 2) + fusc((n + 1) / 2)
