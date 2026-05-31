def solution(elements):
    n = len(elements)
    doubled = elements * 2  # 배열 2배
    result = set()

    for length in range(1, n):       # 부분 수열 길이: 1 ~ n-1
        for start in range(n):       # 시작 위치: 0 ~ n-1
            s = sum(doubled[start:start + length])
            result.add(s)

    return len(result)+1