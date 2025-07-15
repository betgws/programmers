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

             


    
solution([10, 10, 10, 40],45)



