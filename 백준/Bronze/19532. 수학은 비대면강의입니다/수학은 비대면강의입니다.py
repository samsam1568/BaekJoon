import sys

arr = list(map(int,sys.stdin.readline().split()))
answer = []

for i in range(-999,1000):
    for j in range(-999,1000):
        if (i*arr[0] + j*arr[1] == arr[2]):
            if (i*arr[3] + j*arr[4] == arr[5]):
                answer.append(i)
                answer.append(j)


print(*answer)


