from collections import deque

A,B = map(int,input().split())

def solution(start,target):
    if start == target:
        return 0
    
    queue = deque([(start, 0)])
    visited = set([start])

    while queue:
        num,cnt = queue.popleft()

        for i in [int(str(num)+"1"), num*2]:
            if i == target:
                return cnt+1
            
            if i < target and i not in visited:
                visited.add(i)
                queue.append((i,cnt+1))
    return -1

result = solution(A, B)
print(-1 if result == -1 else result + 1)
