from collections import defaultdict
from itertools import combinations
import bisect

def solution(info, query):
    score_map = defaultdict(list)

    # 1. info 전처리
    for i in info:
        parts = i.split()
        keys = parts[:-1]
        score = int(parts[-1])

        # 4개의 속성 중에서 '-' 조합 포함 모든 조합 (2^4)
        for n in range(5):  # 0~4개를 -로 대체
            for comb in combinations(range(4), n):
                temp = keys[:]
                for idx in comb:
                    temp[idx] = "-"
                key = ' '.join(temp)
                score_map[key].append(score)

    # 2. 각 리스트를 정렬 (이진 탐색을 위한 정렬)
    for key in score_map:
        score_map[key].sort()

    result = []
    for i in query:
        i = i.replace(" and", "")
        q_Parts = i.split()
        key= " ".join(q_Parts[:-1])
        score = int(q_Parts(-1))

        if key in score_map:
            scoreList = score_map[key]
            idx = bisect.bisect_left(scoreList, score)
            result.append(len(score)- idx)
        else:
            result.append(0)

    return result