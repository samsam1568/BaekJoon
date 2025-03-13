import math
import sys

N, K = map(int,sys.stdin.readline().rstrip().split())

if K < 0 or K > N:
    print(0)
else:
    print(int(math.factorial(N)/( math.factorial(K) * math.factorial(N-K) )))