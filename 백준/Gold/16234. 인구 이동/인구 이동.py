from collections import deque
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def bfs(a, L, R): # check 만들고 탐색하면 좌표 저장하고 인구이동
  n = len(a)
  c = [[False] * n for _ in range(n)]
  ok = False
  for i in range(n):
    for j in range(n):
      if c[i][j] == False:
        q = deque()
        q.append((i, j))
        c[i][j] = True
        s = [(i,j)]
        total = a[i][j]
        while q:
          x, y = q.popleft()
          for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if 0 <= nx < n and 0 <= ny < n and c[nx][ny] == False:
              diff = abs(a[x][y] - a[nx][ny])
              if L <= diff <= R:
                q.append((nx, ny))
                c[nx][ny] = True
                s.append((nx, ny))
                total += a[nx][ny]
                ok = True
        for x,y in s:
          a[x][y] = total // len(s)
  return ok

N, L, R = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(N)]
ans = 0
while True:
  if bfs(a, L, R):
    ans += 1
  else:
    break
print(ans)


