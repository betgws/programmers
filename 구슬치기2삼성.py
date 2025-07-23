from collections import deque

def solution():
    # 첫 줄 입력
    N, M = map(int, input().split())  
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    # N줄 보드 입력
    board = [input().strip() for _ in range(N)]  
    # R, B 위치 찾기
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'R':
                R1 = (i, j)
            elif board[i][j] == 'B':
                B1 = (i, j)
            
    def bfs():
        queue = deque()
        queue.append([R1, B1, 1])

        while queue:
            R, B, dist = queue.popleft()

            if dist >= 11:
                return -1

            for dx, dy in directions:
                # **방향마다 원래 좌표로 초기화**
                tempR = [R[0], R[1]]
                tempB = [B[0], B[1]]

                # **빨간 구슬 굴리기**
                while board[tempR[0]+dx][tempR[1]+dy] == ".":
                    tempR[0] += dx
                    tempR[1] += dy

                # **파란 구슬 굴리기**
                while board[tempB[0]+dx][tempB[1]+dy] == ".":
                    tempB[0] += dx
                    tempB[1] += dy

                # **구멍 체크 — '0'이 아니라 'O' (알파벳 O)**
                if board[tempB[0]+dx][tempB[1]+dy] == "O":
                    continue
                elif board[tempR[0]+dx][tempR[1]+dy] == "O":
                    return dist

                # **큐에 넣을 때 tuple/list 한 번에**
                queue.append([tuple(tempR), tuple(tempB), dist+1])

        return -1

    answer = bfs()
    print(answer)  # 결과 출력 (문제는 보통 출력 요구하니까)

solution()
