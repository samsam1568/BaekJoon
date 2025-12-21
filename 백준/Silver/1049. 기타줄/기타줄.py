
N, M = map(int, input().split())
one_package = 999999999999
six_package = 999999999999

for j in range(M):
    a,b = map(int, input().split())



    if a < six_package:
        six_package = a

    if b < one_package:
        one_package = b

target = 0
answer = 0
while target < N:
    if one_package* 6 < six_package:
        answer += one_package*N
        target = N

    else:
        if (N-target) * one_package > six_package:
           answer += six_package
           target += 6

        else:
            answer += one_package
            target += 1


print(answer)

