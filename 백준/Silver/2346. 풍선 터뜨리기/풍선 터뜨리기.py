import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
moves = list(map(int, input().split()))

dq = deque((i + 1, moves[i]) for i in range(N))

order = []

# 첫 풍선 터뜨리기
idx, step = dq.popleft()
order.append(idx)

while dq:
    if step > 0:
        dq.rotate(-(step - 1))
    else:
        dq.rotate(-step) 

    idx, step = dq.popleft()
    order.append(idx)

print(*order)