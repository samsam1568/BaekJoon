import sys


arr = list(sys.stdin.readline().rstrip())
tmp = ""
i = 0
while i < len(arr):
    tmp = arr[i:i+10]
    for j in tmp:
        print(j,end="")
    print()
    i += 10