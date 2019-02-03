def queue_time(customers, n):
    solution=[0]*n
    for i in customers:
        solution[solution.index(min(solution))]+=i
    return max(solution)
