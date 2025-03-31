import sys

a,b,c,d = map(int,sys.stdin.readline().rstrip().split())

answer= min(a,b,c-a,d-b)

print(answer)

