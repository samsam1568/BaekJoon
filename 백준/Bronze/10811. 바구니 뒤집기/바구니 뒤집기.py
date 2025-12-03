from collections import deque

N, M = map(int, input().split())
target = [i for i in range(1, N + 1)]
arr = [list(map(int, input().split())) for i in range(M)]
for start, end in arr:
    tmp = list(reversed(target[start-1:end]))
    target = target[:start-1] + tmp + target[end:]


for j in target:
    print(j, end = " ")