import sys
from collections import deque
from itertools import combinations, permutations

N = int(input())
num_list = list(map(int,sys.stdin.readline().split()))
ms = list(map(int,sys.stdin.readline().split()))
result_list = []
idx = 0
temp = []

for i in ms:
    if (idx==0):
        for j in range(i):
            temp.append("+")
    if (idx==1):
        for j in range(i):
            temp.append("-")

    if (idx==2):
        for j in range(i):
            temp.append("*")
    if (idx==3):
        for j in range(i):
            temp.append("/")
    idx += 1
ms_list = deque(set(permutations(temp,N-1)))
while ms_list:
    value_list = deque(ms_list.popleft())
    now_value = num_list[0]
    num_idx = 1
    while value_list:

        q = value_list.popleft()
        if q == "+":
            now_value = now_value + num_list[num_idx]

        if q == "-":
            now_value = now_value - num_list[num_idx]

        if q == "*":
            now_value = now_value * num_list[num_idx]

        if q == "/":
            if now_value // num_list[num_idx] < 0:
                now_value = -(abs(now_value) // abs(num_list[num_idx]))
            else:
                now_value = now_value // num_list[num_idx]

        num_idx += 1
    result_list.append(now_value)
print(max(result_list))
print(min(result_list))

