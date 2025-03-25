import sys

N = sys.stdin.readline().rstrip()
arr = []

for i in N:
    arr.append(int(i))

arr.sort(reverse=True)
answer = ""
for j in arr:
    answer += str(j)
print(int(answer))