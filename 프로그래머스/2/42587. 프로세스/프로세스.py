from collections import deque

def solution(priorities, location):
    # 1. (우선순위, 원래 위치)를 튜플로 묶어 큐 생성
    # 예: priorities=[2, 1, 3, 2] -> queue=[(2,0), (1,1), (3,2), (2,3)]
    queue = deque([(v, i) for i, v in enumerate(priorities)])
    
    order = 0  # 실행 순서 카운트
    
    while queue:
        current = queue.popleft()  # 일단 맨 앞의 작업을 꺼냄
        
        # 2. 큐에 남아있는 작업들 중 현재보다 우선순위가 높은 게 있는지 확인
        if any(current[0] < item[0] for item in queue):
            # 더 높은 게 있다면 다시 뒤로 보냄
            queue.append(current)
        else:
            # 3. 현재 작업이 가장 우선순위가 높다면 실행(출력)
            order += 1
            # 만약 방금 실행한 작업의 인덱스가 찾고자 하는 location이라면 반환
            if current[1] == location:
                return order

print(solution([2, 1, 3, 2], 2))  # 결과: 1
print(solution([1, 1, 9, 1, 1, 1], 0))  # 결과: 5