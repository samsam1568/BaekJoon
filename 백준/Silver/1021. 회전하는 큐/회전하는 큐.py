import sys
from collections import deque

N, M = map(int,sys.stdin.readline().split())
arr = deque([i for i in range(1,N+1)])
index = list(map(int,input().split()))


count = 0
for i in index:
    while True:
        if i == arr[0]:
            arr.popleft()
            break
        else:
            if arr.index(i) <= len(arr)//2:
                arr.rotate(-1)
            else:
                arr.rotate()

            count += 1
print(count)
