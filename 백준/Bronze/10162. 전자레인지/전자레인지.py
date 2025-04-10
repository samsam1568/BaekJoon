import sys

changes = [300,60,10]
N = int(sys.stdin.readline().rstrip())
res = []
for i in changes:
    res.append(N//i)
    N = N%i
if N == 0:
    print(*res)
else:
    print(-1)