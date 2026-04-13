N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]

arr.sort(key=lambda x : (x[1], x[0]))


for a,b in arr:
    print(a,b)