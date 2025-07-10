def solution(answers):
    answer = []
    a1 = [1,2,3,4,5]
    a2 = [2,1,2,3,2,4,2,5]
    a3 = [3,3,1,1,2,2,4,4,5,5]
    
    score1 = 0
    score2 = 0
    score3 = 0
    
    for i in range(len(answers)):
        if answers[i] == a1[i%5]:
            score1 +=1
        if answers[i] == a2[i%len(a2)]:
            score2 +=1
        if answers[i] == a3[i%len(a3)]:
            score3 +=1
            
    max_score = max(score1, score2, score3)
    if score1 == max_score:
        answer.append(1)
    if score2 == max_score:
        answer.append(2)
    if score3 == max_score:
        answer.append(3)
    return answer