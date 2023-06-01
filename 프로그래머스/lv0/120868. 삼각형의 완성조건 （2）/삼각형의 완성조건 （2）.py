def solution(sides):
    answer = 0
    maxLeg = max(sides)
    
    leg = maxLeg-min(sides)+1
    while leg <= maxLeg:
        if min(sides) + leg > maxLeg:
            answer += 1
        leg += 1
    
    answer += sum(sides)-maxLeg-1
    
    return answer