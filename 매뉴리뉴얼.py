from collections import defaultdict
from itertools import combinations

# 쓰레기 
def solution(orders, course):
    answer = []
    alpha = set()
    dic = {}

    # 모든 알파벳 체크
    for i in orders:
        for j in i:
            alpha.add(j)

    alpha = sorted(list(alpha))


    # 모든 알페벳의 course 조합 찾기 
    for i in course:
        com = ["".join(c) for c in combinations(alpha, i)]
        for j in com:
            dic[j] = 0
        # order 마다 돌면서 개수 체크
        for k in orders:
            can = ["".join(c) for c in combinations(k,i)]
            for p in can:
                dic[p] += 1

        # value 기준으로 정렬하고 append
        sorted_list = sorted(dic.items(), key= lambda x: x[1], reverse= True)
        max = sorted_list[0][1]
        n = 0
        while(sorted_list[n][1] == max):
            a = sorted_list[n][1]
            answer.append(a)
            a += 1
        dic = {}

    return answer


solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4])



# 옳게 된 정딥
from collections import defaultdict
from itertools import combinations

def solution(orders, course):
    answer = []

    for c in course:
        comb_counter = defaultdict(int)

        # 각 주문에서 길이 c 조합을 만들어 카운트
        for order in orders:
            sorted_order = sorted(order)
            for comb in combinations(sorted_order, c):
                comb_counter["".join(comb)] += 1

        # 조합이 없으면 continue
        if not comb_counter:
            continue

        # 최대 등장 횟수 찾기
        max_count = max(comb_counter.values())

        # 2번 이상 등장한 조합 중에서 최대 등장 조합들만 추가
        if max_count >= 2:
            for menu, count in comb_counter.items():
                if count == max_count:
                    answer.append(menu)

    return sorted(answer)
