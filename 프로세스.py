from collections import deque

def solution(priorities, location):
    answer = 0
    locationList = deque()

    priorities = deque(priorities)
    
    for i in range(len(priorities)):
        locationList.append(i)
        
    
    while(priorities):
        a = priorities.popleft()
        
        index = locationList.popleft()
        if(priorities and a < max(priorities)):
            priorities.append(a)
            locationList.append(index)

        else:
            answer = answer + 1
            if(index == location):
                break

        
        
    return answer

solution([1, 1, 1, 1, 1, 1],5)