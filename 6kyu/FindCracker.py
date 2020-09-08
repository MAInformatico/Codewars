def find_hack(arr):
    result = list()

    for i in range(len(arr)) :
        prevScore = arr[i][1]
        sumScore = 0
        
        if prevScore > 200 :
            result.append(arr[i][0])
            continue
                
        if gradeCheck(arr[i][2]) :
            sumScore += 20

        for j in range(len(arr[i][2])) :
            sumScore += convertScore(arr[i][2][j])
            if sumScore > 200 :
                sumScore = 200
                break
        
        if prevScore != sumScore :
            result.append(arr[i][0])
            
    return result

def gradeCheck(valuesList) :
    if( len(valuesList) < 5 ) : 
        return False

    for i in range(len(valuesList)) :
        if valuesList[i] != 'A' and valuesList[i] != 'B' :
            return False
    return True
    
def convertScore(score) :
    return change(score)
    
def change(value) :
    return {
        'A' : 30,
        'B' : 20,
        'C' : 10,
        'D' : 5
    }.get(value, 0) 
