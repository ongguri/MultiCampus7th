def solution(spell, dic):
    answer = 0
    spell.sort()
    
    for w in dic:
        if len(w) == len(spell):
            if sorted(list(w)) == spell:
                return 1
        
    return 2