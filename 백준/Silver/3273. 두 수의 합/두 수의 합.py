import sys

N = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
x = int(sys.stdin.readline())
arr.sort()
i = 0
j = len(arr)-1
answer = 0
while i < j:
    tmp = arr[i] + arr[j]
    if tmp == x:
        answer += 1
        i += 1

    if tmp > x:
        j -= 1

    if tmp < x:
        i += 1

print(answer)