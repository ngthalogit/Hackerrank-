n = int(input())
strings = []
for i in range(n):
    strings.append(input())
quer = []
q = int(input())
for i in range(q):
    quer.append(input())
rs = []
for i in quer:
    rs.append(strings.count(i))
for i in rs:
    print(i)
