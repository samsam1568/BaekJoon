N, M = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(N)]

mt = 1  

def solution(x, y, size):
    if x + size - 1 >= M:
        return
    if y + size - 1 >= N:
        return

    if arr[y][x] == arr[y][x + size - 1] == arr[y + size - 1][x] == arr[y + size - 1][x + size - 1]:
        return size * size

    return 0

for y in range(N):
    for x in range(M):
        for size in range(1, min(N - y, M - x) + 1):
            mt = max(mt, solution(x, y, size))

print(mt)