from collections import deque

def solution(players, m, k):
    answer = 0

    queue = deque()
    for i in range(k):
        queue.append(0)
    
    for i in players:
        p = 0
        q = queue.popleft()
        if(i<(q+1)*m):
            queue.append(0)
        else:
            while(i>=(p+q+1)*m):
                p = p+1
            for j in range(len(queue)):
                a = queue.popleft()
                queue.append(a+p)
            queue.append(p)     

            answer = answer + p

    return answer

solution([0, 2, 3, 3, 1, 2, 0, 0, 0, 0, 4, 2, 0, 6, 0, 4, 2, 13, 3, 5, 10, 0, 1, 5],3,5)