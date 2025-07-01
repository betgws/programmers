from collections import deque

def solution(stages, N):
    answer =[]
    stages.sort()
    stages = deque(stages)
    
    dic = {}
    for i in range(N):
        dic[i+1] = 0.0
    

    while(stages):
        stageLength = len(stages)
        criter = stages.popleft()
        n = 1 

        while(stages and stages[0] == criter):
            stages.popleft()
            n += 1

        if(1<=criter<=N):
            dic[criter] = n / stageLength

    sorted_items = sorted(dic.items(),key=lambda x: x[1],reverse=True)

    for i in sorted_items:
        answer.append(i[0])


    return answer

solution([2, 1, 2, 6, 2, 4, 3, 3],5)