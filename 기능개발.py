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



from collections import deque 


def solution2(progresses, speeds):

    answer = []

    due = deque()

    for i in range(len(progresses)):
        n = (100 - progresses[i])//speeds[i]
        if((100 - progresses[i]) % speeds[i]):
            n = n + 1

        due.append(n)

    while(due):
        n = 1
        criteria = due.popleft()
        while(due and due[0] <= criteria):
            due.popleft()
            n = n + 1

        answer.append(n)


solution2([93, 30, 55],[1, 30, 5])


        
