N,M = map(int, input().split())
R,C,D = map(int, input().split())
location = (R,C)
board = [list(map(int, input().split())) for i in range(N)]

# 북쬭을 보고 있다는 가정하에 북동남서
dir = [(-1,0),(0,1),(1,0),(0,-1)]


while True:

    r , c = location[0], location[1]
    if(board[r][c] == 0 ):
        board[r][c] = 2
    
    notClean = 0
    # 인접 4칸에 안 닦은 칸이 있는지 확인 
    for dr, dc in dir:
        nr, nc = r + dr, c + dc
        if board[nr][nc] == 1 or board[nr][nc] == 2:
            continue
        else:
            notClean += 1
            break

    if(notClean >= 1):

        # 반 시계 방향으로 회전
        d = (d -1) % 4

        # 그 방향에서의 앞 방향
        dr, dc = dir[d]
        nr, nc = r + dr, c + dc

        # 그 방향이 청소하지 않은 빈칸인 경우 한 칸 전진한다.
        if(board[nr][nc] == 0):
            r,c = nr,nc


    else: 
        #바라보는 방향을 유지한채로 한 칸 후진할 수 있으면 한칸 후진
        bd = (d+2)%4
        dr, dc = dir[bd]
        nr, nc = r+dr, c+dc
        if(board[nr][nc] == 0 or board[nr][nc] == 2):
            r,c = nr, nc
        elif(board[nr][nc] == 1):
            break 


             

