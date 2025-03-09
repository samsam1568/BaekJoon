import sys

arr = list(map(int,sys.stdin.readline().rstrip().split()))
answer = 0
for i in arr:
    answer += i**2
answer = answer % 10
print(answer)