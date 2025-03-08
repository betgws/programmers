from collections import deque


def solution(n, results):

    winList =[[]for _ in range(n+1)]
    loseList = [[] for _ in range(n+1)]
    answer = 0

    for i in results:
        winList[i[0]].append(i[1])
        loseList[i[1]].append(i[0])

    
    for i in range(n):

        visited = [False]*(n)
        visited[i] = True

        winQueue = deque()
        winQueue.append(i+1)

        loseQueue = deque()
        loseQueue.append(i+1)

        c = 1
        t = 0
    

        while(winQueue):
            if(c == n):
                answer = answer + 1
                t = 1
                break

            a = winQueue.popleft()
            
            for i in winList[a]:
                if(visited[i-1] == False):
                    visited[i-1] = True
                    c = c+1
                    winQueue.append(i)
        

        while(loseQueue and t == 0):

            if(c == n):
                answer = answer + 1
                t = 1
                break

            a = loseQueue.popleft()
            
            for i in loseList[a]:
                if(visited[i-1] == False):
                    visited[i-1] = True
                    c = c+1
                    loseQueue.append(i)

        if(t == 0 and c == n):
            answer = answer +1
        


    return answer




solution(5,[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]])
