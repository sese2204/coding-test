from itertools import permutations

def solution(k, dungeons):
    answer = -1
    
    for perm in permutations(dungeons):
        cur = k
        count = 0
        
        for min, con in perm:
            if cur >= min:
                count += 1
                cur -= con
            else:
                break # 탐험 종료
        
        answer = max(count, answer)
        
    return answer