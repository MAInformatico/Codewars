def checkMovement(spi,i,j,roti,rotj):
    l = len(spi)
    i += roti
    j += rotj

    if i < 0 or i >= l or j<0 or j >= l:
        return False
    
    if spi[i][j] == 1:
        return False
    
    i += roti
    j += rotj
    
    if i < 0 or i >= l or j<0 or j >= l:
        return True
    
    if spi[i][j] == 1:
        return False
    
    return True  
        
def spiralize(size):
    if size == 0: return []    
    elif size == 1: return[[1]]
    elif size == 2: return[[1,1][0,1]]
    
    spiral = [[0 for i in range(size)] for j in range(size)]
    
    i = j = 0
    
    roti, rotj = 0,1
    
    rotated = 0
    while rotated < 2:
        spiral[i][j] = 1
        
        if checkMovement(spiral,i,j,roti,rotj):
            i+=roti
            j+=rotj
            rotated = 0
        else:
            roti, rotj = rotj, -roti
            rotated += 1
            
    roti,rotj = -rotj, roti
    if spiral[i+roti][j+rotj] == 1:
        spiral[i][j] = 0
    
    return spiral
