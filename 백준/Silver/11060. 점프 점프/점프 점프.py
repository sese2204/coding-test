N = int(input())
a = [0] + list(map(int, input().split()))
d = [-1] * (N+1)
d[0] = 0
d[1] = 0
for i in range(2, N+1):
  for j in range(1,i):
    if (i-j <= a[j]) and d[j] != -1:
      if d[i] == -1:
        d[i] = d[j]+1
      else:
        d[i] = min(d[i], d[j]+1)
print(d[N])