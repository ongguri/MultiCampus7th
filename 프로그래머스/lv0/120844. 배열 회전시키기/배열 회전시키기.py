def solution(numbers, direction):
    if direction == "right":
        answer = numbers[:-1]
        answer.insert(0, numbers.pop())
    elif direction == "left":
        answer = numbers[1:]
        answer.append(numbers[0])
    return answer