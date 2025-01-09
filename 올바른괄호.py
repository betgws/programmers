def solution(s):
    
    stack = []
    
    for i in s:
        if (len(stack) <= 0 and i == ")"):
            return False
        
        elif (i == "("):
            stack.append(i)

        elif (i == ")"):
            stack.pop()

    
    if(len(stack) > 0):
        return False
    
    
    return True

solution(")()(")