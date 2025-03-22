import sys

A = int(sys.stdin.readline().rstrip())
B = int(sys.stdin.readline().rstrip())
C = int(sys.stdin.readline().rstrip())
D = int(sys.stdin.readline().rstrip())
P = int(sys.stdin.readline().rstrip())

X = A*P
if P <= C:
    Y = B
else:
    Y = B + (P-C)*D

price = min(X,Y)
print(price)




