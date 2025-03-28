import sys

N = int(sys.stdin.readline().rstrip())
five, three = N//5+1, 0
mymin = 9999999
while True:
    if N % 5 == 0:
        if N//5 < mymin:
            mymin = N//5
        break
    five -= 1
    three = (N-(five*5))//3
    if five == -1:
        break

    if (five * 5) + (three * 3) == N:
        if five+three < mymin:

            mymin = five+three
            break

    if N % 3 == 0:
        if N // 3 < mymin:
            mymin = N//3

if mymin == 9999999:
    print(-1)
else:
    print(mymin)





