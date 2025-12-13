import sys

E,S,M = map(int,sys.stdin.readline().split())


for i in range(1,999999):
    if E == (i-1)%15 + 1 and S == (i-1)%28+1 and M == (i-1)%19+1:
        print(i)
        break