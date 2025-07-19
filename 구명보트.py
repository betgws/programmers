from collections import deque

def solution(people, limit):
    
    answer = 0 

    people.sort()
    people = deque(people)

    while people:
        big = people.pop()

        if(people and big + people[0] <= limit):
            people.popleft() 

        answer += 1


    return answer 


             
from collections import deque

def solution(people, limit):

    people.sort(reverse = True)
    people = deque(people)
    answer = 0
    i = 0
    while(people):
        current = people.popleft()

        while(current <= limit):
            
            if(people):
                a = people[-1]
            else:
                answer = answer + 1
                break
            if(a+current > limit):
                answer = answer+1
                break
            else:
                people.pop()
                answer = answer +1
                break
    return answer

    
solution([10, 10, 10, 40],45)



