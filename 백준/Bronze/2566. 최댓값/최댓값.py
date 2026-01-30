a = [list(map(int, input().split())) for _ in range(9)]

max = 0
x = 0
y = 0
for i in range(9):
    for j in range(9):
        if a[i][j] >= max:
            x , y = i, j
            max = a[i][j]


print(max)
print(x+1, y+1)
