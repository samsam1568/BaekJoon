import sys

N, M = map(int, sys.stdin.readline().split())
mydic = dict()
for j in range(N):
    site, password = map(str, sys.stdin.readline().split())
    mydic[site] = password

for k in range(M):
    problem = sys.stdin.readline().rstrip()
    print(mydic[problem])