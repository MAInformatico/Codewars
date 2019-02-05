def contain_all_rots(strng, arr):   
    rot = strng
    if not len(arr) or not strng:
        return True

    for i in range(len(strng)):
        if rot  not in arr:
            return False

        init_l = rot[0]
        rot = rot[1:]
        rot += init_l

    return True
