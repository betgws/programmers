def solution(id_list, report, k):
    answer = []
    dic = {}
    dic2 = {}
    for index, i in enumerate(id_list):
        dic[i] = 0
        dic2[i] = set()

    for i in report:
        user, target = i.split()
        dic2[target].add(user)


    for i in dic2:
        if(len(dic2[i]) >= k):
            for j in dic2[i]:
                dic[j] = dic[j]+1 

    for i in dic:
        answer.append(dic[i])
    
    return answer

solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2)