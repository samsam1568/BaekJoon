import sys

def gcd(a,b):
    if a % b == 0:
        return b
    elif b == 0:
        return a
    else:
        return gcd(b, a%b)

A1, B1 = map(int,sys.stdin.readline().split())
A2, B2 = map(int,sys.stdin.readline().split())

A1 = A1*B2
A2 = A2*B1

top = A1+A2
bottom = B1*B2
N = gcd(top,bottom)
print(top//N, bottom//N)