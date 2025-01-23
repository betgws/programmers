import heapq

def solution(jobs):

    priority_queue = []
    priority_request = []
    answer = []

    clock = 0

    for i in range(len(jobs)):
        jobs[i].append(i)

    for i in jobs:
        heapq.heappush(priority_request,(i[0], i[1],i[2]))


    while(priority_queue or priority_request):

    
        while(priority_request and clock >= priority_request[0][0]):
                a = heapq.heappop(priority_request)
                heapq.heappush(priority_queue,(a[1],a[0],a[2]))

        if(priority_queue):
            b = heapq.heappop(priority_queue)
            clock = clock + b[0]
            answer.append(clock - b[1])
        else:
            clock = clock + 1 


    total = sum(answer)
    
    return total // len(answer)

solution([[0, 3], [1, 9], [3, 5]])

    




    

    