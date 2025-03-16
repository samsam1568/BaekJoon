import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
mi = [int(sys.stdin.readline().rstrip()) for _ in range(N)]  # 목표 수열
stack = []  # 스택 역할
result = []  # +, - 기록용
current = 1  # 1부터 N까지의 수

for target in mi:
    while current <= target:  # target이 나올 때까지 push
        stack.append(current)
        result.append("+")
        current += 1

    if stack[-1] == target:  # target을 pop할 수 있으면 pop
        stack.pop()
        result.append("-")
    else:  # 불가능한 경우
        print("NO")
        exit()

print("\n".join(result))
