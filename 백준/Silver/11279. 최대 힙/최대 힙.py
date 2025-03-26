import heapq
import sys

N = int(sys.stdin.readline().rstrip())
arr = []

for i in range(N):
    x = sys.stdin.readline().rstrip()
    if x == "0":
        if len(arr) == 0:
            print(0)
        else:
            print(-heapq.heappop(arr))
    else:
        heapq.heappush(arr,-int(x))
