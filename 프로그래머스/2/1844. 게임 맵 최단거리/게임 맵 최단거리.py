from collections import deque
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
def solution(maps):
    
    def bfs(x, y):
        queue = deque()
        queue.append((x,y))
        while queue:
            x, y = queue.popleft()
            for k in range(4):
                nx, ny = x+dx[k], y+dy[k]
                if 0 <= nx <len(maps) and 0 <= ny <len(maps[0]):
                    if maps[nx][ny] == 1:
                        queue.append((nx,ny))
                        maps[nx][ny] = maps[x][y] + 1
    bfs(0,0)
    
    answer = maps[-1][-1]
    if answer == 1:
        answer = -1
    return answer