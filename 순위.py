def solution(n, results):
    # 그래프 초기화 (0: 알 수 없음, 1: 이김, -1: 짐)
    graph = [[0] * (n + 1) for _ in range(n + 1)]
    
    # 경기 결과 반영
    for winner, loser in results:
        graph[winner][loser] = 1  # 승리
        graph[loser][winner] = -1  # 패배

    # 플로이드-워셜 알고리즘 수행
    for k in range(1, n + 1):  # 중간 선수
        for i in range(1, n + 1):  # 출발 선수
            for j in range(1, n + 1):  # 도착 선수
                if graph[i][k] == 1 and graph[k][j] == 1:
                    graph[i][j] = 1  # i가 j를 이김
                    graph[j][i] = -1  # j는 i에게 짐

    # 정확한 순위를 알 수 있는 선수 수 계산
    answer = 0
    for i in range(1, n + 1):
        count = sum(1 for j in range(1, n + 1) if graph[i][j] != 0)
        if count == n - 1:  # 다른 모든 선수와 승패가 결정됨
            answer += 1

    return answer
