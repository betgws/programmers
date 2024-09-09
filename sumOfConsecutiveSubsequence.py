from collections import deque

def solution(sequence, k):
    
    answer = []
    d = deque()
    sum = 0
    index = 0 
    answerList = []
    
    while (index <= len(sequence)-1):
  

        if(sum < k):
            sum += sequence[index]
            d.append(index)
            index += 1
            
        while(sum > k):

            popIndex = d.popleft()
            sum = sum - sequence[popIndex]
            
        if(sum == k):
            
            answerList.append((d[0],d[-1]))
            popIndex = d.popleft()
            sum = sum - sequence[popIndex]
        
    
    if(sequence[-1] == k):
        answerList.append((len(sequence)-1,len(sequence)-1))        
    sortedList = sorted(answerList, key = lambda x:x[1]-x[0])
        
    answer = list(sortedList[0])

    print(answer)

    
    return answer

solution([1, 1, 1, 2, 2, 4,7],11)