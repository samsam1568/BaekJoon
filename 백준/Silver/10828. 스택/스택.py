import sys

N = int(sys.stdin.readline().strip())
stack = []
for i in range(N):
    order = sys.stdin.readline().strip()

    if "push" in order:
        a, b = order.split()
        stack.append(int(b))
    elif order == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)
    elif order == "size":
        print(len(stack))
    elif order == "empty":
        if not stack:
            print("1")
        else:
            print("0")

    elif order == "pop":
        if not stack:
            print(-1)
        else:
            print(stack.pop())
