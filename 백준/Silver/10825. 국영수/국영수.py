import sys

N = int(sys.stdin.readline())
arr = []
for i in range(N):
    arr.append(list(map(str, sys.stdin.readline().split())))

for j in range(N):
    arr[j][1] = int(arr[j][1])
    arr[j][2] = int(arr[j][2])
    arr[j][3] = int(arr[j][3])

arr.sort(key = lambda x: (-x[1], x[2], -x[3], x[0]))

for k in arr:
    print(k[0])