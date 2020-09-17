import numpy as np

def area_polygon(vertex):
    x = []
    y = []
    for i in range(len(vertex)):
        x.append(vertex[i][0])
        y.append(vertex[i][1])
    
    return round(0.5*np.abs(np.dot(x,np.roll(y,1))-np.dot(y,np.roll(x,1))),1)
