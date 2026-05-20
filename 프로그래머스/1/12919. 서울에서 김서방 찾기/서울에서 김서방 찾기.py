def solution(seoul):
    answer = ''
    for idx,value in enumerate(seoul):
        if value == "Kim":
            answer = "김서방은 " + str(idx) +"에 있다"
            break
    return answer