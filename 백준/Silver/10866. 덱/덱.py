import sys
from collections import deque

arr = deque()
N = int(sys.stdin.readline().rstrip())
for i in range(N):
    order = sys.stdin.readline().rstrip()
    if order == "front":
        if len(arr) > 0:
            print(arr[0])
        else:
            print(-1)
    if order == "back":
        if len(arr) > 0:
            print(arr[-1])
        else:
            print(-1)

    if order == "size":
        print(len(arr))

    if order == "empty":
        if len(arr) == 0:
            print(1)
        else:
            print(0)

    if order == "pop_front":
        if len(arr) > 0:
            print(arr.popleft())
        else:
            print(-1)
    if order == "pop_back":
        if len(arr) > 0:
            print(arr.pop())
        else:
            print(-1)

    if " " in order:
        order1, order2 = order.split()
        if order1 == "push_front":
            arr.appendleft(order2)
        if order1 == "push_back":
            arr.append(order2)


