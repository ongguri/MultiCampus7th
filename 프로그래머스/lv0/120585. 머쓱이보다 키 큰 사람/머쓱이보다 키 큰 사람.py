def solution(array, height):
    answer = 0
    for i in array:
        if(i > height):
            break
        answer += 1
    return len(array) - answer