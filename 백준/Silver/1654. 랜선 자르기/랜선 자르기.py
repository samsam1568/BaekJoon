N, K = map(int, input().split())

arr = list()
for i in range(N):
    arr.append(int(input()))
mymin = 1
mymax = max(arr)
mid = 1

while mymin <= mymax:
    mid = (mymin + mymax) // 2


    tmp = 0
    for j in range(N):
        tmp += arr[j] // mid

    if tmp < K:
        mymax = mid - 1  # 경계 조정: -1
    else:
        mymin = mid + 1  # 경계 조정: +1

print(mymax)
