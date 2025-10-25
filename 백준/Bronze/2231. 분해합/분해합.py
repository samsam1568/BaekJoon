import sys

N = int(sys.stdin.readline())
number_list = []
answer = -999


for i in range(0,N+1):
    number_list = []
    a = str(i)
    for j in range(len(a)):
        number_list.append(int(a[j]))
    tmp = i
    for k in number_list:
        tmp += + k

    if tmp == N:
        answer = i
        break

if answer == -999:
    print(0)
else:
    print(answer)

