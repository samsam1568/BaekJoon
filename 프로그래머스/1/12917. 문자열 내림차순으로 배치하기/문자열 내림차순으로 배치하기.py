def solution(s):
    answer = ''
    a = list()
    for i in s:
        a.append((ord(i),i))
    a.sort(key = lambda x:x[0],reverse = True)
    for idx,value in a:
        answer += value
    return answer