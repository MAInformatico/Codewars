def chess_board_cell_color(cell1, cell2):
    con = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8}
    v1=con[cell1[0]]
    v11=int(cell1[1])    
    v2=con[cell2[0]]
    v21=int(cell2[1])
    b1=True
    b2=True
    if v1%2 != v11%2:
        pass
    else:
        b1=False
    if v2%2 != v21%2:
        pass
    else:
        b2=False
    if b1==True and b2==True or b1!=True and b2!=True:
        return True
    else:
        return False
