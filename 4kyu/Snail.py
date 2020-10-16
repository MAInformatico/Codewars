def snail(snail_map):
    result = []
    totalLength = len(snail_map) - 1
    width = len(snail_map[0])
    lpos = 0
    wpos = -1
    while totalLength >= 0 and width > 0:
        if width > totalLength:
            if wpos >= (len(snail_map[0])) / 2:
                for i in range(width):
                    wpos -= 1
                    result.append(snail_map[lpos][wpos])
            else:
                for i in range(width):
                    wpos += 1
                    result.append(snail_map[lpos][wpos])
            width -= 1
        else:
            if lpos >= (len(snail_map)) / 2:
                for i in range(totalLength):
                    lpos -= 1
                    result.append(snail_map[lpos][wpos])
            else:
                for i in range(totalLength):
                    lpos += 1
                    result.append(snail_map[lpos][wpos])
            totalLength -= 1
    return result
