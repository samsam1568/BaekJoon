N, M = map(int, input().split())
arr = list(map(int, input().split()))

l = 0
r = 0
ans = 0

while(r<N):
    k = sum(arr[l:r+1])

    if k == M:
        ans += 1
        r += 1
    elif k > M:
        l += 1
    else:
        r += 1
print(ans)