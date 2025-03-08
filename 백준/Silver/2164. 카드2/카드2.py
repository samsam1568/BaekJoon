from collections import deque
import sys

N = int(sys.stdin.readline().rstrip())
arr = deque()
for i in range(1,N+1):
    arr.append(i)

while len(arr) > 1:
    arr.popleft()
    arr.append(arr.popleft())
print(*arr)