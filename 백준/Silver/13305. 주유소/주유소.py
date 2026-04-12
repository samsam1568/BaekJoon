import math
import sys

N = int(sys.stdin.readline())
lLoad = list(map(int,sys.stdin.readline().split()))
pOil = list(map(int,sys.stdin.readline().split()))
oil_min = math.inf
ans = 0
for idx in range(N-1):
    oil_min = min(oil_min,pOil[idx])
    ans += oil_min * lLoad[idx]

print(ans)







