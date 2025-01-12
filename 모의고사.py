import math

def solution(answers):

    answerList = [0,0,0]


    A = [1,2,3,4,5]*math.ceil(len(answers)/5)
    B =  [2,1,2,3,2,4,2,5]*math.ceil(len(answers)/8)
    C = [3,3,1,1,2,2,4,4,5,5]*math.ceil(len(answers)/10)

    for i in range(len(answers)):
        if(A[i] == answers[i]):
            answerList[0] += 1

        if(B[i] == answers[i]):
            answerList[1] += 1

        if(C[i] == answers[i]):
            answerList[2] += 1

    result = []
    
    # 가장 높은 점수를 계산
    max_score = max(answerList)


    for i, score in enumerate(answerList):
        if score == max_score:
            result.append(i+1)


   
    return result

solution([1,3,2,4,2])