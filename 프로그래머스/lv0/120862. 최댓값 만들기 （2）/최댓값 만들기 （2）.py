def solution(numbers):
    answer = 0
    
    for i in range(len(numbers)-1):
        if i == 0:
            answer = numbers[i] * numbers[i+1]
        for j in range(i+1, len(numbers)):
            if numbers[i]*numbers[j] > answer:
                answer = numbers[i]*numbers[j]
                
    return answer