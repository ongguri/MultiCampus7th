def solution(num_list, n):
    answer = []
    li = []
    for i in num_list:
        li.append(i)
        if len(li) == n:
            answer.append(li)
            li = []
    return answer