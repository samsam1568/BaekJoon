import sys

N = int(sys.stdin.readline().rstrip())
a = 1
cnt = 0
while True:
    if '666' in str(a):
        cnt += 1

    if cnt == N:
        print(a)
        break
    a += 1



