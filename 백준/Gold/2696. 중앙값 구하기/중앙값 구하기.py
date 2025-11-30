import sys
input = sys.stdin.readline

T = int(input().strip())

for _ in range(T):
    M = int(input().strip())
    target = []
    medians = []
    read_count = 0

    while read_count < M:
        nums = list(map(int, input().split()))
        for x in nums:
            if read_count >= M:
                break

            target.append(x)
            read_count += 1

            if read_count % 2 == 1:
                temp = sorted(target)
                median = temp[len(temp)//2]
                medians.append(median)

    print(len(medians))
    for idx,value in enumerate(medians, start=1):
        print(value, end = " ")
        if idx>10 and idx % 10 ==0:
            print()

