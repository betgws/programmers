def solution(targets):
    
    sortByEnd = sorted(targets, key=lambda t: t[1])
    answer = 0
    lastEnd = -1 
    
    for i in sortByEnd:
        
        if i[0] >= lastEnd:
            
            answer += 1
            lastEnd = i[1]
    
    return answer