import sys
input = sys.stdin.readline

# 1. rstrip()으로 개행문자 제거 필수
s = input().rstrip().upper()

letter = set(s)
l_count = dict()

for l in letter:
    l_count[l] = s.count(l)

# 2. max라는 변수명 대신 max_val 사용
if not l_count: # (방어 코드) 만약 빈 줄이 들어오면 에러 방지
    print('?') # 혹은 예외처리
    exit()

max_val = max(l_count.values())

max_l = ''
result_count = 0 # 3. 변수명 명확하게 (최댓값과 최댓값의 등장 횟수 구분)

for k, v in l_count.items():
    if v == max_val:
        result_count += 1
        max_l = k

if result_count == 1:
    print(max_l)
else:
    print('?')