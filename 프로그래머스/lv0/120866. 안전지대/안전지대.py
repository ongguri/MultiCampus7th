def dangerArea(board, line, area):
    if board[line][area] == 0:
        board[line][area] = -1
    if board[line][area+1] == 0:
        board[line][area+1] = -1
    if board[line][area-1] == 0:
        board[line][area-1] = -1
    return board

def solution(board):
    answer = 0

    board.insert(0, [0]*len(board[0]))
    board.append([0]*len(board[0]))

    for line in board:
        line.insert(0, 0)
        line.append(0)  
    
    for line in range(len(board)):
        for area in range(len(board[line])):
            if board[line][area] == 1:
                board = dangerArea(board, line, area)
                board = dangerArea(board, line+1, area)
                board = dangerArea(board, line-1, area)

    for i in range(1, len(board)-1):
        answer += board[i][1:len(board[i])-1].count(0)
    
    return answer