import sys

i = [0 for _ in range(30)]
arr = [int(sys.stdin.readline().rstrip()) for _ in range(28)]
for j in arr:
    i[j-1] += 1

answer= []

for idx,value in enumerate(i):
    if value == 0:
        answer.append(idx+1)

for k in answer:
    print(k)