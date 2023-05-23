def solution(numer1, denom1, numer2, denom2):
    denom = denom1*denom2
    numer = numer1*denom2 + numer2*denom1
    
    for i in range(numer, 1, -1):
        if denom % i == 0 and numer % i == 0:
            numer //= i
            denom //= i

    return [numer, denom]
