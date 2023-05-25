def solution(emergency):
    answer = [0] * len(emergency)
    
    for i in range(len(emergency)):
        locateMaxNum = emergency.index(max(emergency))
        answer[locateMaxNum] += i+1
        emergency[locateMaxNum] = 0
    return answer