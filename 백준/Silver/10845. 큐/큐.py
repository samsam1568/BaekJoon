import collections
import sys

N = int(sys.stdin.readline().rstrip())
dq = collections.deque()

for i in range(N):
    mt = sys.stdin.readline().rstrip()
    if "push" in mt:
        #두자리 명령
        A,B = mt.split()
        dq.append(int(B))

    else:
        A = mt
        if A == "pop":
            if len(dq) > 0:
                print(dq.popleft())
            else:
                print(-1)

        elif A == "front":
            if len(dq) > 0:
                print(dq[0])
            else:
                print(-1)

        elif A == "back":
            if len(dq) > 0:
                print(dq[-1])
            else:
                print(-1)

        elif A == "size":
            print(len(dq))
        elif A == "empty":
            if len(dq) == 0:
                print(1)
            else:
                print(0)

