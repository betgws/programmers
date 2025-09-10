H, W, N, M = map(int, input().split())

board = [[0]*W for _ in range(H)]

total = 0
# 모든 방향 
direction = [(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)]

for r in range(len(board)):
    for s in range(len(board[0])):
        if(board[r][s] == 0):
            board[r][s] = 1
            total += 1

            for i in direction:
                nr = r + i[0]
                ns = s + i[1]

                if( 0<= nr < H and 0<= ns < W):
                    board[nr][ns] += 1


print(total)

