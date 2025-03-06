def dfs(idx):
    if idx == M:
        for i in range(len(arr)):
            print(arr[i],end=" ")
        print()
    else:
        for j in range(1,N+1):
            if visited[j-1]:
                continue
            visited[j-1] = True
            arr[idx] = j
            dfs(idx+1)
            visited[j-1] = False

N, M = map(int,input().split())
visited = [False] * N
arr = [0]*M
dfs(0)