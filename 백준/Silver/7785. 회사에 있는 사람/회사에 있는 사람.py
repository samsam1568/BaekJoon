import sys

N = int(sys.stdin.readline())
mydic = dict()

for i in range(N):
    people, state = map(str, sys.stdin.readline().split())
    mydic[people] = state

ans = []

for name,value in mydic.items():
    if value == "enter":
        ans.append(name)

ans.sort(reverse=True)
for i in ans:
    print(i)