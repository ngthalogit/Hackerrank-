q = int(input())
s1, s2 = [], [] 
while q:
    s = input().split()
    t = int(s[0])
    if t == 1:
        x = int(s[1])
        s1.append(x)
    else:
        if len(s2) == 0:
            while s1:
                s2.append(s1.pop())
        if t == 2:
            s2.pop()
        if t == 3:
            print(s2[-1])
    q -= 1
