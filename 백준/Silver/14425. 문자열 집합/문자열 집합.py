import sys

N,M = map(int,sys.stdin.readline().rstrip().split())

mydic = set()
for i in range(N):
    mydic.add(sys.stdin.readline().rstrip())

check_list = list()
for j in range(M):
    check_list.append(sys.stdin.readline().rstrip())
answer = 0

for k in check_list:
    if k in mydic:
        answer += 1


print(answer)