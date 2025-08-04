from itertools import combinations

N = int(input())
board = [list(map(int,input().split)) for _ in range(N)]

total = 0 
min = 999999
HN = N // 2
Nlist = []

# 전체 값 찾기
for i in board:
    total += sum(i)

# com 을 위한 Nlist 만들기
for i in range(N):
    Nlist.append(i)


# 조합마다 값 찾고 최소값과 비교
for team in combinations(HN, Nlist ):
    ri = 0
    for inside in combinations(2, team):
        for i,j in inside:
            ri += board[i]
            ri += board[j]

    other = total - ri 

    if(min >= abs(other - ri)):
        min = abs(other - ri)

    






