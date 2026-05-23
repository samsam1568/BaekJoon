def solution(s):
    answer = True
    mylist = []
    for i in s:
        if i == "(":
            mylist.append(i)
        else:
            if mylist == []:
                answer = False
                break
            mylist.pop()

    if len(mylist) > 0:
        answer = False

    return answer