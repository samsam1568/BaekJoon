import sys

N,M = map(int,sys.stdin.readline().rstrip().split())
arr1=set()
arr2=set()

for i in range(N):
    arr1.add(sys.stdin.readline().rstrip())
for j in range(M):
    arr2.add(sys.stdin.readline().rstrip())
answer = []

for i in arr1:
    if i in arr2:
        answer.append(i)

answer.sort()
print(len(answer))

for k in answer:
    print(k)
