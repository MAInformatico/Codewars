import itertools
def get_pins(observed):
    adjacentnumbers = {
        '1': ['2', '4'],
        '2': ['1', '3', '5'],
        '3': ['2', '6'],
        '4': ['1', '5', '7'],
        '5': ['2', '4', '6', '8'],
        '6': ['3', '5', '9'],
        '7': ['4', '8'],
        '8': ['5', '7', '9', '0'],
        '9': ['6', '8'],
        '0': ['8'],
    }
    all=[[digit]+adjacentnumbers[digit] for digit in observed]
    return [''.join(i) for i in list(itertools.product(*all))]  
