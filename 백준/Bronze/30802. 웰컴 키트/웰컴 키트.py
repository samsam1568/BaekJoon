import sys

N = int(sys.stdin.readline().rstrip())
arr = list(map(int,sys.stdin.readline().rstrip().split()))
T, P = map(int,sys.stdin.readline().rstrip().split())
answer = 0
for i in arr:
    if i == 0:
        continue
    if i <= T:
        answer += 1
    else:
        answer += i//T
        if i % T > 0:
            answer += 1

print(answer)
print(N//P, N%P)