import sys

N = int(sys.stdin.readline().rstrip())
arr = []
for _ in range(N):
    x,y = map(int,sys.stdin.readline().rstrip().split())
    arr.append([x,y])

arr.sort(key=lambda x: x[1])
arr.sort(key=lambda x: x[0])
for i in arr:
    print(*i)