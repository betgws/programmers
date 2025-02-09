def solution(numbers, target):

   
    answer = []

    def dfs(cnt,n):

        str = "-+"

        if cnt == len(numbers):
            if(n == target):
                answer.append(1)
            return 
        for i in str:
            if(i == "-"):
                dfs(cnt+1,n - numbers[cnt])
            elif(i == "+"):
                dfs(cnt+1,n + numbers[cnt])

               
    dfs(0,0)
        
   
    return len(answer)

solution([4, 1, 2, 1],4)