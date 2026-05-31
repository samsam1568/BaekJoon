def solution(s):
    answer = 0
    x = ""
    x_count = 0
    n_count = 0
    
    for i in s:
        
        # x 지정
        if x_count == 0 and n_count == 0:
            x = i
            x_count += 1

        elif x == i:
            x_count += 1
            
        elif x != i:
            n_count += 1
            
        if x_count != 0 and x_count == n_count:
            x = ""
            x_count,n_count = 0,0
            answer += 1
    
    if x_count > 0:
        answer += 1
            
    return answer