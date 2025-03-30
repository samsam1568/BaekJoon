import sys

A,B = map(int,sys.stdin.readline().rstrip().split())
C = int(sys.stdin.readline().rstrip())

if B+C >= 60:
    A += (B+C)//60
    B = (B+C) % 60
elif B+C < 60:
    B = B+C
if A >= 24:
    A -= 24
print(A,B)

