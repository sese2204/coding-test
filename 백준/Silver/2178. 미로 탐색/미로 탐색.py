from collections import deque
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
n, m = map(int,input().split())
a = [list(map(int,list(input()))) for _ in range(n)]


q = deque()
q.append((0, 0))
while q:
  x, y = q.popleft()
  for k in range(4):
    nx, ny = x + dx[k], y + dy[k]
    if 0 <= nx < n and 0 <= ny < m:
      if a[nx][ny] == 1:
        q.append((nx, ny))
        a[nx][ny] = a[x][y] + 1
print(a[n-1][m-1])