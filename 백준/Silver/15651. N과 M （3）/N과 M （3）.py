import sys


def dfs(idx):
    if idx == M:
        for i in arr:
            print(i, end=" ")
        print()
    else:
        for j in range(1,N+1):
            arr[idx] = j
            dfs(idx+1)

N,M = map(int,sys.stdin.readline().rstrip().split())
arr = [0] * M
dfs(0)


