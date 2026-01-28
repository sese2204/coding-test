import math

def solution(progresses, speeds):
    answer = []
    days = []
    
    # 각 작업의 남은 일수 계산
    for i in range(len(progresses)):
        # (100 - 진행률) / 속도 -> 올림 처리
        d = math.ceil((100 - progresses[i]) / speeds[i])
        days.append(d)
    
    max_day = days[0]
    count = 0
    
    for day in days:
        if day <= max_day:
            # 기준일(max_day)보다 빨리 끝나거나 같으면 함께 배포
            count += 1
        else:
            # 기준일보다 오래 걸리는 작업 -> 기존 작업 배포, 기준일 변경, count 초기화
            answer.append(count)
            max_day = day
            count = 1
            
    answer.append(count)
    
    return answer