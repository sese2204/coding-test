def solution(numbers, target):
    global answer
    answer = 0
    def go(i, total):
        global answer
        if i == len(numbers):
            if total == target:
                answer += 1
            return
        go(i+1, total+numbers[i])
        go(i+1, total-numbers[i])
    go(0,0)
    return answer
