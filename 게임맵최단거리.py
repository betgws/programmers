from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # 동, 서, 남, 북 방향 이동 정의
    
    # BFS 함수 정의
    def bfs(x, y):
        queue = deque([(x, y, 1)])  # 시작점과 이동 거리를 큐에 저장
        
        while queue:
            x, y, dist = queue.popleft()
            
            # 상대 팀 진영에 도착한 경우
            if x == n - 1 and y == m - 1:
                return dist
            
            # 동서남북 네 방향으로 이동
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                # 맵 범위 내에서 벽이 아닌 곳으로 이동
                if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                    maps[nx][ny] = 0  # 방문 처리 (재방문 방지)
                    queue.append((nx, ny, dist + 1))
        
        # 상대 팀 진영에 도달할 수 없는 경우
        return -1
    
    # 시작점에서 BFS 탐색
    return bfs(0, 0)
