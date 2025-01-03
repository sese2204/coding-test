def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command[0], command[1], command[2]
        slicedArray = sorted(array[i-1:j])
        answer.append(slicedArray[k-1])
    
    return answer