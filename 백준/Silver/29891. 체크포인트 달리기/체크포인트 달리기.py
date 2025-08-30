import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
arr = []
for i in range(n):
    a = int(sys.stdin.readline().rstrip())
    arr.append(a)
# arr = set(arr)
# arr = list(arr)
arr.sort()
tot = 0
k = n - 1
while k >= 0:
    tot += abs(arr[k]) * 2
    k -= m
print(tot)