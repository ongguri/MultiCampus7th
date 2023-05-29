def solution(keyinput, board):
    answer = [0, 0]
    xMax, xMin, yMax, yMin = board[0]//2, -(board[0]//2), board[1]//2, -(board[1]//2)
    
    for i in keyinput:
        if i == "left" and xMin < answer[0]:
            answer[0] -= 1
        elif i == "right" and answer[0] < xMax:
            answer[0] += 1
        elif i == "down" and yMin < answer[1]:
            answer[1] -= 1
        elif i == "up" and answer[1] < yMax:
            answer[1] += 1
    
    return answer