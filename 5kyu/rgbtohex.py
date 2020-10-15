def rgb(r, g, b):
    round = lambda i: min(255, max(i, 0))
    return ("{:02X}" * 3).format(round(r), round(g), round(b))
