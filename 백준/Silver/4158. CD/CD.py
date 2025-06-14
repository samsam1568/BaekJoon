
while True:
    N, M = map(int,input().split())
    if N == 0 and M == 0:
        break

    sang, sun = [], []

    for _ in range(N):
        sang.append(int(input()))

    for _ in range(M):
        sun.append(int(input()))
    answer = 0

    while sang:
        target = sang.pop()
        lt, rt = 0, M - 1
        while lt <= rt:
            idx = (lt + rt)//2

            if target == sun[idx]:
                answer += 1
                break

            elif target > sun[idx]:
                lt = idx + 1

            else:
                rt = idx - 1

    print(answer)
