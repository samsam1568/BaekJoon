n, L = map(int, input().split())
arr = list(map(int, input().split()))
tmp = 0
num = 0
for i in range(n-1, 0, -1):
    tmp += arr[i]
    num += 1

    mid = tmp / num

    if arr[i-1] <= mid - L or arr[i-1] >= mid + L:
        print("unstable")
        break

    if i == 1:
        print("stable")

