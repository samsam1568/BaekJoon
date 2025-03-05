import sys

N = int(sys.stdin.readline().strip())

for i in range(N):
    word = sys.stdin.readline().strip()
    stack = []
    tmp = True
    for j in word:
        if j == "(":
            stack.append(j)
        else:
            if len(stack) == 0 or j == stack.pop():
                print("NO")
                tmp = False
                break

    if len(stack) > 0:
        tmp = False
        print("NO")

    if tmp:
        print("YES")



