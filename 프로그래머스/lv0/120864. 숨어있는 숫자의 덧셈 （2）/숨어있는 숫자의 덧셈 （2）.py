def solution(my_string):
    answer = 0
    num = ''
    
    for i in my_string:
        if i.isdigit():
            num += i
        elif i.isalpha() and len(num) != 0:
            answer += int(num)
            num = ''
    if len(num) != 0:
        answer += int(num)
        
    return answer