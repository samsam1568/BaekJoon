import sys

statement = sys.stdin.readline().rstrip()

arr_minus = statement.split("-")
for idx,value in enumerate(arr_minus):
    if "+" in value:
        tmp = 0
        arr_plus = list(value.split("+"))
        for j in arr_plus:
            tmp += int(j)
        arr_minus[idx] = str(tmp)

answer = 0
for k in range(len(arr_minus)):
    if k == 0:
        answer += int(arr_minus[k])
    else:
        answer -= int(arr_minus[k])
print(answer)