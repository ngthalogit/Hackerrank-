n = int(input())
stack = list()
tmp = -10000
while n:
    strings = input()
    t = int(strings.split(' ')[0])
    if t == 1:
        x = int(strings.split(' ')[-1])
        stack.append(x)
        tmp = max(tmp, x)
    if t == 2:
        last = stack[-1]
        stack.pop()
        if last == tmp:
            if len(stack) != 0:
                tmp = max(stack)
            else:
                tmp = -10000
    if t == 3:
        print(tmp)
    n -= 1
            
    
