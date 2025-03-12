import sys

T = int(sys.stdin.readline().rstrip())
for test_case in range(T):
    k = int(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline().rstrip())

    arr = [[0 for _ in range(15)] for _ in range(15)]

    for p in range(15):
        arr[0][p] = (p+1)

    for i in range(1, k + 1):  # 1층부터 k층까지
        arr[i][0] = 1  # 각 층의 1호는 항상 1명
        for j in range(1, n):  # 2호부터 n호까지
            arr[i][j] = arr[i][j - 1] + arr[i - 1][j]  # 점화식 적용
    print(arr[k][n-1])







# 1 4(1+2+1) 10(1+2+1+1+2+3) 20 35
# 1 3(1+2) 6(1+2+3) 10(1+2+3+4) 15(1+2+3+4+5)
# 1 2 3 4 5