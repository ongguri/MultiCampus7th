def solution(num_list):
    answer = [0, 0]
    for i in num_list:
        if i == 0 or i % 2 == 0: answer[0] += 1
        else: answer[1] += 1
    return answer