def solution(brown, yellow):

    answer = []
    yellowMList = []
    canBrownList = []

    for i in range(yellow):
        if(yellow % (i+1) == 0):
            yellowMList.append((i+1, yellow//(i+1)))

    sortedYList = [tuple(sorted(t,reverse=True)) for t in yellowMList]
    sortedYList = set(sortedYList)

    for i in sortedYList:
        if(i[0]*2 + i[1]*2+4 == brown):
            canBrownList.append(i)
            break

    answer.append(canBrownList[0][0]+2)
    answer.append(canBrownList[0][1]+2)
    return answer

solution(24,24)  