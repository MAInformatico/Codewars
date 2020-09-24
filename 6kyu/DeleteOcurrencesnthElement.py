def delete_nth(order,max_e):
    if not order or max_e < 1:
        return []
    
    counted_order = { i:0 for i in order }
    result = []

    for i in order:
        if counted_order[i] < max_e:
            counted_order[i] += 1
            result.append(i)

    return result
