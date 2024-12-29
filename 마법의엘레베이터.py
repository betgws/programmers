def solution(storey):
    answer = 0

    while storey:

        dev = storey%10

        if ((dev == 5 and (storey//10)%10 >= 5) or (dev >5)):
            storey = storey + 10 - dev
            answer = answer + 10 - dev

        else: 
            answer = answer + dev
        
        storey= storey//10






    
    return answer