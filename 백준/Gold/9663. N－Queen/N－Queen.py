import sys

N = int(sys.stdin.readline().rstrip())
chess = [0 for _ in range(N)]
ans = 0
def is_promising(x):
    # 이번 열에 놓을 수 있는 지 확인
    for i in range(x):
        if chess[x] == chess[i] or abs(chess[x]-chess[i]) == abs(x-i):
            return False
    return True

def N_queen(x):
    global ans
    if x == N:
        ans += 1
        return

    else:
        for i in range(N):
            chess[x] = i
            if is_promising(x):
                N_queen(x+1)
N_queen(0)
print(ans)

