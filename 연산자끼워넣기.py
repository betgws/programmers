N = map(int, input().split())
num = list(map(int, input().split()))
p, m, t, q = map(int, input().split())

# 더하기 배기 곱하기 나누기
operator = [p,m,t,q]
answer = []

def DFS(now, remain, ind):

    if(sum(remain) == 0):
        answer.append(now)
        return 
    
    for oI, o in enumerate(operator):

        if(o > 0):
            if(oI == 0):
                operator[oI] -= 1
                DFS(now + num[ind], operator, ind+1)
                operator[oI] += 1
            elif(oI == 1):
                operator[oI] -= 1
                DFS(now - num[ind], operator, ind+1)
                operator[oI] += 1
            elif(oI == 2):
                operator[oI] -= 1
                DFS(now * num[ind], operator, ind+1)
                operator[oI] += 1
            elif(oI == 3):
                operator[oI] -= 1
                DFS(now // num[ind], operator, ind+1)
                operator[oI] += 1





        
        


