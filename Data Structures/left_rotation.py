n, d = [int(i) for i in input().split(' ')]
arr = [int(i) for i in input().split(' ')]

while d:
    arr.append(arr[0])
    del arr[0]
    d -= 1
for i in arr:
    print(i, end=' ')
