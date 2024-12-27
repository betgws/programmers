def solution(x, y, n):


    answer1 = 100000001
    answer2 = 100000001

    type1 = y - n
    type2 = y 

    if(type1 % x == 0):
        answer1 = 0 
        answer1 = answer1 + 1
        answer1 = divide_by(type1//x, answer1)

    if(type2 % x == 0):
        answer2 = 0
        answer2 = divide_by(type2//x,answer2)

    if((type1 % x != 0) and (type2 % x != 0)):
        return -1
    
    elif(answer1 == 100000001 and answer2 == 100000001):
        return -1
    
    elif((type1 % x != 0) and answer2 == 100000001):
        return -1
    
    elif(answer1 == 100000001 and (type2 % x != 0)):
        return -1
    else:
        return min(answer1, answer2)

    
        


def divide_by(a, answer):


    while(a%2 == 0):
        answer  = answer + 1 
        a = a // 2
    while(a%3 == 0):
        answer = answer + 1
        a = a // 3

    if (a != 1) :
        return 100000001
    
    else:
        return answer
    
solution(2,17,3)
       


        
