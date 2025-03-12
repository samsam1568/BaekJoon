import sys

M = int(sys.stdin.readline().rstrip())
N = int(sys.stdin.readline().rstrip())

tmp = []

for i in range(M,N+1):
    if i == 1:
        continue
    check = True
    for j in range(2,(i//2)+1):
        if i % j == 0:
            check = False
            break

    if check:
        tmp.append(i)

if tmp:
    print(sum(tmp))
    print(min(tmp))
else:
    print(-1)

