def validBraces(string):
    checker = []
    dictBraces = {"{":"}", "[":"]", "(":")", "}":"{", "]":"[", ")":"("}
    for i in range(len(string)):
        if string[i] == "(" or string[i] == "[" or string[i] == "{":
            checker.append(string[i])
        else:
            if len(checker) == 0:
                return False
            if dictBraces[string[i]] == checker[len(checker)-1]:
                del checker[len(checker)-1]
            else:
                return False
    if len(checker) != 0:
        return False
    return True
