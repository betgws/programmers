from collections import defaultdict

def solution(genres, plays):

    answer = []
    
    hashmap = defaultdict(list)
    hashmap2 = defaultdict(int)
    
    for i in range(len(genres)):
        hashmap[genres[i]].append((plays[i],i))
        hashmap2[genres[i]] += plays[i]

    #많이 재생된 순으로 정렬    
    for key in hashmap:
        hashmap[key] = sorted(hashmap[key], key=lambda x:x[0],reverse = True)

    # 장르별로 많이 재생된 순으로 정렬
    hashmap2 = sorted(hashmap2.items(), key=lambda x: x[1], reverse=True)

    for key,value in hashmap2:
        if(len(hashmap[key]) == 1):
            answer.append(hashmap[key][0][1])

        else:
            answer.append(hashmap[key][0][1])
            answer.append(hashmap[key][1][1])


    return answer

solution(["classic", "pop", "classic", "classic", "pop"],[500, 600, 150, 800, 2500])







        