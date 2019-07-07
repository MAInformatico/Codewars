def count(string):
    if not string:
        return {}
    if string:
        res = dict()
        for c in string:
            if c in res.keys():
                res[c] = res[c] + 1
            else:
                res[c] = 1
        return res
