N = int(input())

arr = []
A = set()
ans = 0
for i in range(N):
    arr.append(input())

for i in arr:
    target = i

    if target == "ENTER":
        ans += len(A)
        A.clear()
    else:
        A.add(i)

ans += len(A)
print(ans)





