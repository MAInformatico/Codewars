def solution(n):
    result = []
    string = list(str(n))
    dictRoman = [['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'],
           ['X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'],
           ['C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'],
           ['M', 'MM', 'MMM', 'MM', 'M', 'MM', 'MMM', 'MMMM', 'MM']
        ]
    for i in range(len(string)):
        if string[i] == '0':
            continue
        else:
            result.append(dictRoman[len(string) - 1 - i][int(string[i]) - 1])      
    return ''.join(result)
