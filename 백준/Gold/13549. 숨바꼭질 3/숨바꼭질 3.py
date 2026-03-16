import sys
from collections import deque

start,goal = map(int,sys.stdin.readline().split())

q = deque()
q.append((start,0))
ans = []
visited = [False for _ in range(100001)]
visited[start] = True

def bfs():
    # 기준으로 잡고 찾아야는 것 = 거리
    # 답은 시간으로 나와야 함
    while q:
        p, t = q.popleft()

        if p > 100000 or p < 0:
            return -1

        for dx, dt in [(p*2, t)]:
            if 0<=dx<=100000 and visited[dx] == False:
                visited[dx] = True
                q.append((dx,dt))

                if dx == goal:
                    ans.append(dt)

        for nx, nt in [(p-1, t+1), (p+1, t+1)]:
            if 0 <= nx <= 100000 and visited[nx] == False:
                visited[nx] = True
                q.append((nx, nt))

                if nx == goal:
                    ans.append(nt)

    return -1

bfs()

if len(ans) == 0:
    print(0)

else:
    print(min(ans))