import sys

N = int(sys.stdin.readline().rstrip())
a = 666
cnt = 0
while True:
    if '666' in str(a):
        cnt += 1

    if cnt == N:
        break
    a += 1
print(a)


