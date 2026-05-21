import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while len(scoville) >= 2:
        m1 = heapq.heappop(scoville)
        if m1 >= K:
            return answer
        
        m2 = heapq.heappop(scoville)
        heapq.heappush(scoville, m1 + 2*m2)
        answer += 1
    
    if scoville[0] < K:
        return -1
    
    return answer