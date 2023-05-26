def solution(my_string):
    answer = ''
    alp = ["a","e","i","o","u"]
    for i in my_string:
        if i not in alp:
            answer += i
    return answer