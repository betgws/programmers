def solution(friends, gifts):
    answer = 0
    dic = {}
    # 선물 준사람을 키로 딕셔너리 만들기 
    for i, f in enumerate(friends):
        dic[f] =  [i] + [0]*len(friends)

    for i in gifts:
        f,s = i.split()
        dic[f][dic[s][0]+1] += 1


    # 선물 지수 계산하기 
    giftRateList = []
    
    for i, f in enumerate(friends):
        give = 0
        take = 0
        for a in range(len(friends)):
            give = give + dic[f][a+1]
        for b in friends:
            take = take + dic[b][i+1]

        giftRateList.append(give-take)
        
    # 누가 가장 많이 받는지 max 값 찾기
    receive_count = [0] * len(friends)

    for i in range(len(friends)):
        for j in range(i+1, len(friends)):  # ← i < j 조건
            f1 = friends[i]
            f2 = friends[j]
            give1 = dic[f1][j+1]  # f1이 f2에게 준 선물 수
            give2 = dic[f2][i+1]  # f2가 f1에게 준 선물 수

            if give1 > give2:
                receive_count[i] += 1
            elif give1 < give2:
                receive_count[j] += 1
            else:
                if giftRateList[i] > giftRateList[j]:
                    receive_count[i] += 1
                elif giftRateList[i] < giftRateList[j]:
                    receive_count[j] += 1


    answer = max(receive_count)
    return answer


solution(["joy", "brad", "alessandro", "conan", "david"],["alessandro brad", "alessandro joy", "alessandro conan", "david alessandro", "alessandro david"])