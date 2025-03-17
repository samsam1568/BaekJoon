import sys

N = int(sys.stdin.readline().rstrip())
num_arr = list(map(int,sys.stdin.readline().rstrip().split()))
M = int(sys.stdin.readline().rstrip())
target = list(map(int,sys.stdin.readline().rstrip().split()))

mydic = dict()
for i in num_arr:
    if i not in mydic:
        mydic[i] = 1
    else:
        mydic[i] += 1
answer = []
for j in target:
    if j in mydic:
        answer.append(mydic[j])
    else:
        answer.append(0)


print(*answer)




