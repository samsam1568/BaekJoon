import sys

N = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))

arr.sort()
answer = float('inf')
answer_list = []

i = 0
j = len(arr)-1
while i < j:
    if abs(arr[i] + arr[j]) < abs(answer):
        answer = arr[i]+arr[j]

        answer_list.clear()
        answer_list.append(arr[i])
        answer_list.append(arr[j])
        answer_list.sort()

    if arr[i] + arr[j] > 0:
        j -= 1
    else:
        i += 1

for i in answer_list:
    print(i, end= " ")