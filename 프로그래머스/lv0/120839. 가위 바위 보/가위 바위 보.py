def solution(rsp):
    win = {'5' : '2', '2' : '0', '0' : '5'}
    return ''.join([win[i] for i in rsp])