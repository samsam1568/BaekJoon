import sys

N = int(sys.stdin.readline())


current_sum = 0

i = 1
while True:
    current_sum += i

    if current_sum > N:
        print(i - 1)
        break

    i += 1