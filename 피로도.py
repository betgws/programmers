def solution(k, dungeons):
    visited = [False] * len(dungeons)
    max_count = 0

    def DFS(remain, dist):
        nonlocal max_count
        max_count = max(max_count, dist)

        for i, (min_required, consumed) in enumerate(dungeons):
            if not visited[i] and remain >= min_required:
                visited[i] = True
                DFS(remain - consumed, dist + 1)
                visited[i] = False

    DFS(k, 0)
    return max_count
