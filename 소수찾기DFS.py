def solution(numbers):
    answer = set()



    def DFS(number,n):

        if(n > len(number)):
            return

        if(number != "" and is_prime(int(number))):
            answer.add(int(number))

        for i in range(len(numbers)):
            if not visited[i]:
                visited[i] = True
                DFS(number+numbers[i],n+1)
                visited[i] = False

    visited = [False] * len(numbers)
    DFS("", 0)
    
    return len(answer)
        

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True



