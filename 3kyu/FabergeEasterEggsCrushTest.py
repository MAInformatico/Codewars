def height(n,m):
    maximalHeight, check = 0, 1
    for i in range(1, n + 1): 
        check = check * (m - i + 1) // i
        maximalHeight += check
    return maximalHeight
