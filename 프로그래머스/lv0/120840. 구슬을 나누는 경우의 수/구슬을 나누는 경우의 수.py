def solution(balls, share):
    # 분자 numer,	분모 denom
    answer = 0
    numer, denom = 1, 1
    for i in range(balls, 0, -1):
        numer *= i
        if i <= balls-share:
            denom *= i
        if i <= share:
            denom *= i
    return numer//denom