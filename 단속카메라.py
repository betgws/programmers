from collections import deque

def solution(routes):

    routes.sort(key = lambda x : x[1])
    routes1 = deque(routes)
    visit = routes1[0]
    answer = 1

    for i in routes:

        if(visit[1] >= i[0]):
                routes1.popleft()

        else:
            answer = answer + 1
            visit = routes1.popleft()



    return answer 

solution([[-20,-15], [-21,-13], [-12,-6], [-5,-3],[-11,-2]])