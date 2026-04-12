import math
import sys

N = int(sys.stdin.readline())
lLoad = list(map(int,sys.stdin.readline().split()))
pOil = list(map(int,sys.stdin.readline().split()))
ans = pOil[0] * lLoad[0]
oil_min = math.inf

for idx in range(1,N-1):
    oil_min = min(oil_min,pOil[idx])
    ans += oil_min * lLoad[idx]

print(ans)







