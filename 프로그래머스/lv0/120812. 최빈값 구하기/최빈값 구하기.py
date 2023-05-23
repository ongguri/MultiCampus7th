def solution(array):
    array.sort()

    idx = 0
    count = 0
    answer = 0

    while idx < len(array):
        numCount = array.count(array[idx])
        if count < numCount:
            count = numCount
            answer = array[idx]
        elif count == numCount:
            answer = -1
        idx += numCount
    return answer