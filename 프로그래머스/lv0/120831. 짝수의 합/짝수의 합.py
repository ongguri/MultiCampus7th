def solution(n):
    answer = 0
    
    for i in range(n, 0, -1):
        if i % 2 == 0: answer += i
    return answer