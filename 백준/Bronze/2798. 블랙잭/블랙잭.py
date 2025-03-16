import sys

N,M = map(int,sys.stdin.readline().rstrip().split())
arr = list(map(int,sys.stdin.readline().rstrip().split()))
mm = 0
for i in range(N):
    for j in range(N):
        for k in range(N):
            if i == j or i == k or j == k:
                continue

            if arr[i] + arr[j] + arr[k] > M:
                continue

            if arr[i] + arr[j] + arr[k] > mm:
                mm = arr[i] + arr[j] + arr[k]
print(mm)
