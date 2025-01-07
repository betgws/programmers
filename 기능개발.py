from collections import deque 
import math

def solution(progresses, speeds):

    answer = []
    stack = []
    

    for i in range(len(progresses)):
        progresses[i] = math.ceil((100- progresses[i])/speeds[i])


    for i in range(len(progresses)):
        if(i == 0):
            stack.append(progresses[i])

        elif(stack[0] >= progresses[i]):
            stack.append(progresses[i])
        else:
            answer.append(len(stack))
            stack = []
            stack.append(progresses[i])
        

    answer.append(len(stack))
    
        
    return answer

solution([85, 80, 90, 85],[5, 5, 5, 5])