def solution(s):
    answer = True
    
    a = []
    for string in s:
        try:
            if string == "(":
                a.append(string)
            else:
                a.pop()
        except:
            return False

    if a:
        return False
    return True