import sys

def isPos(a):
    check = 0
    for i in a:
        if i > 0:
            check += 1

    if check == len(a):
        return True

    return False

def isNeg(a):
    check = 0
    for i in a:
        if i < 0:
            check += 1

    if check == len(a):
        return True

    return False



n, m = map(int, sys.stdin.readline().rstrip().split())
arr = []
for i in range(n):
    a = int(sys.stdin.readline().rstrip())
    arr.append(a)
arr.sort()
tot = 0
k = n - 1

while len(arr) >= m:
    tmp = []
    for k in range(m):
        tmp.append(arr.pop())
    if isPos(tmp):
        tot += max(tmp)*2

    elif isNeg(tmp):
        tot += abs(min(tmp))*2

    else:
        tot += max(tmp)*2
        tot += abs(min(tmp))*2

if len(arr) > 0:
    if isPos(arr):
        tot += max(arr)*2

    elif isNeg(arr):
        tot += abs(min(arr))*2

    else:
        tot += max(arr)*2
        tot += abs(min(arr))*2

print(tot)


