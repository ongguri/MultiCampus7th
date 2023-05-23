def solution(n):
    
    for i in range(min(6, n), 0, -1):
        if 6 % i == 0 and n % i == 0:
            piece = 6 // i
            n = n // i
            break
    return (piece * n * i) // 6