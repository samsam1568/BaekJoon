import sys


N = int(sys.stdin.readline().rstrip())
arr = set(map(int,sys.stdin.readline().rstrip().split()))
M = int(sys.stdin.readline().rstrip())
marr = list(map(int,sys.stdin.readline().rstrip().split()))

for i in marr:
    if i in arr:
        print(1)
    else:
        print(0)