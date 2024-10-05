def solution(picks, minerals):

    answer = 0
    tempList = []
    a = 0
    totalPicks = 0
    
    need = len(minerals)//5
    if len(minerals)%5 > 0:
        need = need + 1

    for aa in picks:
        totalPicks = totalPicks+aa



    newMineralList = chunk_list5(minerals, 5)

    while(need > totalPicks):
        newMineralList.pop()
        need = len(newMineralList)//5
        


    for mineralListPart in newMineralList:
        temp = 0
        for mineralPart in mineralListPart:
            if(mineralPart == "diamond"):
                temp = temp + 25
            elif(mineralPart == "iron"):
                temp = temp + 5
            else:
                temp = temp + 1

        tempList.append((temp,a))
        a = a+1
    
    tempList.sort(key=lambda x:x[0], reverse=True)

    for i in range(len(newMineralList)):
        
        nowList = newMineralList[tempList[i][1]]

        if(picks[0] > 0):
            answer = answer + 5
            picks[0] = picks[0] - 1

        elif(picks[1]> 0 ):
            for iron in nowList:
                if(iron == "diamond"):
                    answer = answer + 5

                else:
                    answer = answer + 1
            picks[1] = picks[1] - 1
        elif(picks[2] > 0):

            for stone in nowList:
                if(stone == "diamond"):
                    answer = answer + 25

                elif(stone == "iron"):
                    answer = answer + 5

                else:
                    answer = answer + 1

            picks[2] = picks[2] - 1
        else:
            break
    print(answer)
    return answer

def chunk_list5(lst, chunk_size):
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]

solution([0, 1, 1],["diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron", "iron", "iron", "iron", "diamond"])