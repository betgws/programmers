from collections import defaultdict

def solution_dfs(tickets):
    graph = defaultdict(list)

    # 그래프 생성 (알파벳 순으로 정렬된 상태로 저장)
    for a, b in sorted(tickets):
        graph[a].append(b)

    route = []  # 결과 경로를 저장할 리스트

    def dfs(airport):
        while graph[airport]:
            next_airport = graph[airport].pop(0)  # 항상 알파벳 순으로 선택
            dfs(next_airport)
        route.append(airport)

    dfs("ICN")
    return route[::-1]  # 역순으로 반환

# 테스트 예시
tickets1 = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
tickets2 = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]

print(solution_dfs(tickets2))  # Output: ['ICN', 'ATL', 'ICN', 'SFO', 'ATL', 'SFO']