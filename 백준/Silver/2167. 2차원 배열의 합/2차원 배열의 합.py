n, m = map(int,input().split())

graph = []

for i in range(n):
    graph.append(list(map(int,input().split())))

dp = [[0] * (m+1) for _ in range(n+1)]

# 누적합 구하기
for i in range(1, n+1):
    for j in range(1, m+1):
        # 누적합 = 본래값 + 왼쪽 누적합 + 오른쪽 누적합 - 대각선 누적합
        dp[i][j] = graph[i-1][j-1] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]

k = int(input())

for _ in range(k):
    i, j, x, y = map(int,input().split())
    # 누적합 이용하여 결과 구하기
    print(dp[x][y] - dp[i-1][y] - dp[x][j-1] + dp[i-1][j-1])