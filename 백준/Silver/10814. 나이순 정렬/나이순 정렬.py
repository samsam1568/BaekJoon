import sys

M = int(sys.stdin.readline().rstrip())
arr = list()
for _ in range(M):
    age,name = map(str,sys.stdin.readline().rstrip().split())
    arr.append([int(age),name])
arr.sort(key=lambda x: x[0])
for i in arr:
    print(*i)