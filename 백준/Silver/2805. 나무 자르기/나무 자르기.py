import sys

N, M = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))

arr.sort()
start = 1
end = max(arr)
mid = 0

while start <= end:
    mid = (start+end)//2

    tmp = 0
    for k in arr:
        gap = k - mid
        if gap > 0:
            tmp += gap

    if tmp >= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)

