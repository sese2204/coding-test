import sys
n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
d = [[0]*n for _ in range(n)]
for i in range(n):
    d[i][i] = True
for i in range(n-1):
    if a[i] == a[i+1]:
        d[i][i+1] = True
for k in range(2, n):
    for i in range(0, n-k):
        j = i+k
        if a[i] == a[j] and d[i+1][j-1]:
            d[i][j] = True
m = int(sys.stdin.readline())
for _ in range(m):
    s,e = map(int,sys.stdin.readline().split())
    print(1 if d[s-1][e-1] else 0)