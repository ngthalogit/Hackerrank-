N, M = [int(i) for i in input().split()]
A = [0 for i in range(N+2)]
for i in range(M):
    a, b, k = [int(i) for i in input().split()]
    A[a] += k
    A[b + 1] -= k
m,v = 0,0
for a in A :
    v += a
    m = max(v, m)
        
print(m)
