from collections import deque
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
n, m = map(int,input().split())
a = [list(map(int,list(input()))) for _ in range(n)]
q = deque()
dist = [[0]*m for _ in range(n)]
q.append((0,0))
dist[0][0]=1
while q:
  x, y = q.popleft()
  for k in range(4):
    nx, ny = x+dx[k], y+dy[k]
    if 0<= nx <n and 0<= ny <m:
      if dist[nx][ny] == 0 and a[nx][ny] == 1:
        q.append((nx,ny))
        dist[nx][ny] = dist[x][y]+1
print(dist[n-1][m-1])