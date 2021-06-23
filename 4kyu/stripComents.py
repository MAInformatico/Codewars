def solution(string,markers):
    aux = string.split('\n')
    for i, line in enumerate(aux):
        for character in markers:
            checker = line.find(character)
            if checker != -1:
                line = line[:checker]
        aux[i] = line.rstrip(' ')
    return '\n'.join(aux)      
