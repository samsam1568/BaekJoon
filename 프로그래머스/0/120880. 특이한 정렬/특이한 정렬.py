def solution(numlist, n):
    answer = []
    mdic = dict()
    for i in numlist:
        if i not in mdic.keys():
            mdic[i] = abs(i-n)
    tmp= list(mdic.items())
    tmp.sort(key = lambda x:(x[1],-x[0]))
    for i,v in tmp:
        answer.append(i)
    return answer