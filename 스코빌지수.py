import heapq

def solution(scoville, K):

    heapq.heapify(scoville)
    min1 = heapq.heappop(scoville)
    num = 0

    while(min1 < K):

        num = num + 1

        if(scoville):
            min2 = heapq.heappop(scoville)
            a = min1 + min2*2
            heapq.heappush(scoville,a)
            min1 = heapq.heappop(scoville)

        else:
            return -1
   
    return num

solution([1, 1, 1],10)