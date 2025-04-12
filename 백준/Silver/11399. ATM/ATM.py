import sys

N = int(sys.stdin.readline().rstrip())
arr = list(map(int,sys.stdin.readline().rstrip().split()))

arr.sort()
tmp = 0
answer = 0
for i in arr:
    tmp += i
    answer += tmp

print(answer)