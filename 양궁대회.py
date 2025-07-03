def solution(n, info):
    currentAnswer = [0]*11
    answer = []
    # 현재 가장 큰 값
    max = 0

    #어피치의 점수
    aScore = 0 
    for i in range(len(info)):
        if(info[i]>0):
            aScore += (10 - i)
    
    use = n 

    def dfs(aScore,score,use,idx,currentAnswer):
       
        if(idx>=10):
            if(use>0):
                currentAnswer[idx] = use
            else:
                if(aScore - score >= max):
                    max = aScore - score
                    answer = currentAnswer[:]
                   
            return 
        
        for i in range(idx, len(info)):

            if(info[i]<= (use-1) and info[i] > 0):
                currentAnswer[i] = info[i] + 1
                dfs(aScore-(10-i),score+(10-i),use - (info[i]+1),i,currentAnswer)
                currentAnswer[i] = 0

            elif(info[i] <= use and info[i] == 0):
                currentAnswer[i] = info[i] + 1
                dfs(aScore,score+(10-i),use - (info[i]+1),i,currentAnswer)
                currentAnswer[i] = 0
                
            

    
    
            
    
            
            
            
    
                
                    

    


    return answer