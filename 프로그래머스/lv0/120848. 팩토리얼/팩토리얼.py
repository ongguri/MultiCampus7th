def factorial(num):
    if num == 1:
        return 1
    return num * factorial(num-1)

def solution(n):
    num = 1
    
    while True:
        result = factorial(num)
        if result > n:
            answer = num-1
            break;
        num += 1
        
    return answer