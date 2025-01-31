from itertools import permutations

def solution(k, dungeons):
    
    all = list(permutations(dungeons))
    realAnswer = 0

    for i in all:
        nk = k
        answer = 0
        for a in i:
            if(a[0]<=nk and nk>0):
                nk = nk - a[1]
                answer = answer + 1

            else:
                break
        if(realAnswer < answer):
            realAnswer = answer
        if(realAnswer == len(dungeons)):
            break
      
    return realAnswer

solution(80,[[80,20],[50,40],[30,10]])