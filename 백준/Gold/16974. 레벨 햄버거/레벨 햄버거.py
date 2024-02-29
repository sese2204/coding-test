n, x = map(int, input().split())

B = [0] * (n+1)
P = [0] * (n+1)

B[0] = 1
P[0] = 1

for i in range(1,n+1):
  B[i] = 2*B[i-1] + 3
  P[i] = 2*P[i-1] + 1

def go(n, x):
  if n == 0:
    return 1
  if x == 1:
    return 0
  elif 2 <= x <= B[n-1] + 1:
    return go(n-1, x-1)
  elif x == B[n-1] + 2 :
    return P[n-1] + 1
  elif B[n-1]+2 < x < 2*B[n-1] + 2 :
    return P[n-1] + 1 + go(n-1, x-B[n-1]-2)
  else:
    return 2*P[n-1] + 1

ans = go(n,x)

print(ans)