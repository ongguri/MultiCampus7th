def solution(lines):
    answer = 0
    
    line1 = range(lines[0][0], lines[0][1]+1)
    line2 = range(lines[1][0], lines[1][1]+1)
    line3 = range(lines[2][0], lines[2][1]+1)
    
    minPoint = min(lines[0][0], lines[1][0], lines[2][0])
    maxPoint = max(lines[0][1], lines[1][1], lines[2][1])

    for p in range(minPoint, maxPoint):
        count = 0
        if p in line1 and p+1 in line1:
            count += 1
        if p in line2 and p+1 in line2:
            count += 1
        if p in line3 and p+1 in line3:
            count += 1

        if count >= 2:
            answer += 1
    return answer