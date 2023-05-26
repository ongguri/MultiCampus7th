def solution(n):
    answer = set()
    s = [2, 3]

    for i in range(5, 10000):
        for j in s:
            if i % j == 0:
                break;
        else:
            s.append(i)
    
    idx = 0
    while n // s[idx] != 0:
        if n % s[idx] == 0:
            answer.add(s[idx])
            n //= s[idx]
        elif n % s[idx] != 0:
            idx += 1
    return sorted(list(answer))