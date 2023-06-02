def solution(a, b):
    answer = 0
    minNum = min(a, b)
    
    num = 2
    while minNum >= num:
        if a % num == 0 and b % num == 0:
            minNum = a // num
            a //= num
            b //= num
        else:
            num += 1
    
    if b == 1: return 1
    
    i = 2
    while i <= b:
        if b % i == 0:
            if i != 2 and i != 5:
                return 2
            b //= i
        else:
            i += 1
            
    return 1