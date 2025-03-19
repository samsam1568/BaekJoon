import sys

N,K = map(int,sys.stdin.readline().rstrip().split())
arr = [i for i in range(1,N+1)]
idx = K-1
answer = []
while True:

    answer.append(arr[idx])
    arr.remove(arr[idx])

    if len(arr) == 0:
        break
    idx = (idx + (K-1)) % len(arr)

print("<",end="")
for i in answer:
    if i == answer[len(answer)-1]:
        print(i,end="")
        continue
    print(i,end = ", ")


print(">")