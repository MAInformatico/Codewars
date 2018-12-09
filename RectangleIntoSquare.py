def sqInRect(lng, wdth):
    if lng == wdth:
        return None
    lista = []
    
    lista.append(min(lng, wdth))
    while lng != wdth:
        minNum = min(lng, wdth)
        maxNum = max(lng, wdth)
        lng = minNum
        wdth = maxNum - minNum
        lista.append(min(lng, wdth))  
    return lista
