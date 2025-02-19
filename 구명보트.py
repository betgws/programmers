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


solution([10,30,40,50,50],50)



