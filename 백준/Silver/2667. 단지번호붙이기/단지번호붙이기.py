import sys
from collections import deque

N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]
house_list = list()
total = 0
house = 0
for i in range(N):
    for j in range(N):

        if arr[i][j] == 1 and visited[i][j] == 0:
            q = deque()
            q.append((i, j))
            house = 1
            visited[i][j] = 1
            while q:
                x,y = q.popleft()
                for dx,dy in [[1,0], [-1,0],[0,1],[0,-1]]:
                    cx, cy = x+dx, y+dy
                    if 0 <= cx <= (N-1) and 0 <= cy <= (N-1) and visited[cx][cy] == 0 and arr[cx][cy] == 1:
                        q.append([cx,cy])
                        visited[cx][cy] = 1
                        house += 1

            total += 1
            house_list.append(house)

print(total)
house_list.sort()

for k in house_list:
    print(k)
