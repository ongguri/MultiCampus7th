def solution(my_string):
    return sum(sorted([int(i) for i in my_string if i.isdigit()]))