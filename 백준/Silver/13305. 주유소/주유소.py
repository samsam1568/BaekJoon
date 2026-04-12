import sys

N = int(sys.stdin.readline())
lLoad = list(map(int,sys.stdin.readline().split()))
pOil = list(map(int,sys.stdin.readline().split()))
ans = pOil[0] * lLoad[0]

for idx in range(1,N-1):
    ans += min(pOil[:idx+1]) * lLoad[idx]

print(ans)







