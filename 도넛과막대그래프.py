def solution(edges):
    answer = []
    dic = {}

    for a,b in edges :
        if not a in dic:
            dic[a] = [0,0]
        if not b in dic:
            dic[b] = [0,0]

