def dfs(idx):
    global arr
    flag = False
    cnt = 0
    if idx == M:
        for i in range(1,M+1):
            if i == M:
                break
            if arr[i] > arr[i-1]:
                cnt += 1
        if cnt == len(arr)-1:
            flag = True
        if flag:
            for k in range(len(arr)):
                print(arr[k], end =" ")
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
arr = [0] * M
dfs(0)

