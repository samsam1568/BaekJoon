import sys

N = int(sys.stdin.readline().rstrip())
arr = set()
for _ in range(N):
    arr.add(int(sys.stdin.readline().rstrip()))
arr2 = list(arr)

arr2.sort()

for i in arr2:
    print(i)