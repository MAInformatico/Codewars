def what_century(year):
    notation = {'1': 'st', '2': 'nd', '3': 'rd'}
    century = str(int(year) // 100 + (1 if int(year) % 100 > 0 else 0))
    return century + (notation.get(century[-1], 'th') if century[0] != '1' else 'th')
