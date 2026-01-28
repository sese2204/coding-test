def solution(arr):
    cur = -1
    answer = []
    # arr의 값과 cur 값이 다르면 cur에 저장
    # 같으면 pop하여 삭제
    for i in range(len(arr)):
        if arr[i] != cur:
            answer.append(arr[i])
            cur = arr[i]
    
    
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    return answer