import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
answer = []

for k in range(N, 0, -1):
    answer.insert(arr[k-1], k)

print(*answer)