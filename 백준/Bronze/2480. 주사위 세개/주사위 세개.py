import sys

a, b, c = map(int,sys.stdin.readline().rstrip().split())
cnt = 0
value = 0
if a == b:
    cnt += 1
    value = a
if a == c:
    cnt += 1
    value = a
if b == c:
    cnt += 1
    value = b

if cnt == 3:
    print(10000 + value*1000)
elif cnt == 1:
    print(1000 + value * 100)
elif cnt == 0:
    print(max(a,b,c) * 100)
