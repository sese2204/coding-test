def solution(brown, yellow):
    answer = []
    for w in range(1, 2500):
        for h in range (1,w+1):
            if (w-2)*(h-2) == yellow and 2*w+2*h-4 == brown:
                answer.append(w)
                answer.append(h)
    return answer