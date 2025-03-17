from collections import deque


def solution(board):
    answer = 0

    #상하좌우
    direction = [(-1,0),(1,0),(0,-1),(0,1)]
    #행
    n = len(board)
    #열
    m = len(board[0])

    visited = [[0]*m for _ in range(n)]

    # R의 위치를 찾기
    for i, row in enumerate(board):
        if "R" in row:
            startn = i
            startm = row.index("R")
            visited[startn][startm] = 1
            break
 
    queue = deque()
    queue.append((startn, startm,0))
    

    while(queue):

        pop = queue.popleft()
        for j in direction:
            TPN = pop[0]
            TPM = pop[1]
            while( 0<= TPN + j[0] < n and 0 <= TPM + j[1] < m and board[TPN+j[0]][TPM+j[1]] != "D" ):
                TPN = TPN+ j[0]
                TPM = TPM + j[1]

                if (not (0 <= TPN + j[0] < n) or not (0 <= TPM + j[1] < m) or board[TPN + j[0]][TPM + j[1]] == "D"):
                    if( visited[TPN][TPM] == 1):
                        break
                    else:
                        visited[TPN][TPM] = 1
                        queue.append((TPN,TPM,pop[2]+1))
                        break

            if(board[TPN][TPM] == "G"):
                return pop[2] +1

    return -1


solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."])