def solution(numer1, denom1, numer2, denom2):
    denom = denom1*denom2
    numer = numer1*denom2 + numer2*denom1

    num = 1
    for i in range(1, numer):
        if denom % i == 0 and numer % i == 0:
            if num < i:
                num = i
    numer //= num
    denom //= num

    if denom % 2 == 0 and numer % 2 == 0:
        numer //= 2
        denom //= 2

    return [numer, denom]