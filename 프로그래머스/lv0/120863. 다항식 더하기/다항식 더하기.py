def solution(polynomial):
    answer = ''
    poly, num = 0, 0
    polyList = polynomial.split(" + ")
    
    for p in polyList:
        if p.isdigit():
            num += int(p)
        else:
            if p == "x": poly += 1
            else: poly += int(p[:-1])
    
    if poly == 0:
        answer = str(num)
    elif num == 0:
        if poly != 1:
            answer = str(poly) + "x"
        else:
            answer = "x"
    else:
        if poly != 1:
            answer = str(poly) + "x" + " + " + str(num)
        else:
            answer = "x" + " + " + str(num)
        
    return answer