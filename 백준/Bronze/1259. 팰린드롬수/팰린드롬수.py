import sys
from collections import deque

while True:
    N = sys.stdin.readline().rstrip()

    if N == "0":
        break

    check = True
    for i in range(len(N)//2):
        if N[i] != N[-(i+1)]:
            check = False
            break

    if check:
        print("yes")
    else:
        print("no")


