def justify(text, width):
    words = text.split()
    current_length = 0
    list_words = []
    matrix = [list_words]
    for i in words:
        if current_length + len(i) > width:
            list_words = [i]
            matrix.append(list_words)
            current_len = len(i) + 1
        else:
            list_words.append(i)
            current_length += len(i) + 1
    for j in range(len(matrix) - 1):
        list_words = matrix[j]
        space_need = width - sum(len(k) for k in list_words)
        while space_need:
            for index in range(len(list_words) - 1):
                if space_need == 0:
                    break
                list_words[index] += ' '
                space_need -= 1
        matrix[j] = ''.join(list_words) + '\n'
    matrix[-1] = ' '.join(matrix[-1])
    return ''.join(matrix)
