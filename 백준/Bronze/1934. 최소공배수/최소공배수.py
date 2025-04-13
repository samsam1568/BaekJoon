import sys


def gcd(a,b):
    while b > 0:
        a, b = b, a % b
    return a
def lcd(a,b):
    i = gcd(a,b)
    return a*b//i
N = int(sys.stdin.readline().rstrip())
for i in range(N):
    a,b = map(int,sys.stdin.readline().rstrip().split())
    print(lcd(a,b))