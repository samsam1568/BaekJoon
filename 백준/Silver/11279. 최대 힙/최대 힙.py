import heapq
import sys

max_heap = []

N = int(sys.stdin.readline())
for i in range(N):
    num = int(sys.stdin.readline())
    if num == 0:
        if len(max_heap) > 0:
            print(-heapq.heappop(max_heap))
        else:
            print(0)

    else:
        heapq.heappush(max_heap,-num)