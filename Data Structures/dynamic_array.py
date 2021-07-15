n, q = [int(x) for x in input().split(' ')]
rs = []
for i in range(n):
    rs.append([])
lastAnswer = 0
while q:
    t, x, y = [int(x) for x in input().split(' ')]
    idx = (x^lastAnswer)%n
    if (t == 1):
        rs[idx].append(y)
    if (t == 2):
        lastAnswer = rs[idx][y%len(rs[idx])]
        print(lastAnswer)
    q = q-1  
