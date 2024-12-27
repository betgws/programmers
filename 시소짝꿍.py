from collections import Counter


def solution(weights):
    answer = 0

    counter = Counter(weights)

    for i, j in counter.items:
        if j >= 2:
            answer = answer + j*(j-1)/2

    weights = set(weights)

    for w in weights:
        if w*2/3 in weights:
            answer = answer + counter[w*2/3]* counter[w]

        if w*2/4 in weights:
            answer+= counter[w*2/4] * counter[w]
            
        if w*3/4 in weights:
            answer+= counter[w*3/4] * counter[w]
        

    return answer