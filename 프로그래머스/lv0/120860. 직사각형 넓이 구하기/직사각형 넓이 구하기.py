def solution(dots):
    dots.sort()
    x = dots[2][0] - dots[0][0]
    y = dots[1][1] - dots[0][1]
    return x*y