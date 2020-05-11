def accum(s):
    return '-'.join((c * i).title() for i, c in enumerate(s, 1))
