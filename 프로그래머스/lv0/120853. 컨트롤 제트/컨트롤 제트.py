def solution(s):
    answer = []
    s = s.split(" ")
    for i in range(len(s)):
        if s[i] == "Z":
            answer.pop()
            continue
        answer.append(int(s[i]))
    return sum(answer)