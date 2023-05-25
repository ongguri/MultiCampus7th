def solution(age):
    answer = ''
    
    # 48 -> 0, 57 -> 9
    # 97 -> a, 122 -> z
    for i in str(age):
        answer += chr(97 + int(i))
    return answer