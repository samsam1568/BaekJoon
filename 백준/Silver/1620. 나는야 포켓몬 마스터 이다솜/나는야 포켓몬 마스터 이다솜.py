import sys

N, M = map(int,sys.stdin.readline().rstrip().split())

arr = dict()
num = dict()
for i in range(N):
    a=sys.stdin.readline().rstrip()
    arr[i+1] = a
    num[a] = i+1

for j in range(M):
    p = sys.stdin.readline().rstrip()
    if p.isdecimal():
        print(arr[int(p)])
    else:
        print(num[p])