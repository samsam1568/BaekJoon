from collections import deque

n=int(input())
v=int(input())
graph = [[] for i in range(n+1)]
visited=[0]*(n+1)

for i in range(v):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited[1]=1
Q = deque([1])
cnt = 0
while Q:
    target = Q.popleft()
    for node in graph[target]:
        if visited[node] == False:
            visited[node] = True
            Q.append(node)
            cnt += 1

print(cnt)