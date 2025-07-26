import heapq

def solution(operations):
    minheap, maxheap = [], []
    visited = {}
    idx = 0

    for op in operations:
        cmd, num = op.split()
        num = int(num)

        if cmd == "I":
            heapq.heappush(minheap, (num, idx))
            heapq.heappush(maxheap, (-num, idx))
            visited[idx] = True
            idx += 1

        elif cmd == "D":
            if num == 1:  # 최대값 삭제
                while maxheap and not visited[maxheap[0][1]]:
                    heapq.heappop(maxheap)
                if maxheap:
                    _, i = heapq.heappop(maxheap)
                    visited[i] = False
            elif num == -1:  # 최소값 삭제
                while minheap and not visited[minheap[0][1]]:
                    heapq.heappop(minheap)
                if minheap:
                    _, i = heapq.heappop(minheap)
                    visited[i] = False

    # 남아 있는 유효 값 정리
    while minheap and not visited[minheap[0][1]]:
        heapq.heappop(minheap)
    while maxheap and not visited[maxheap[0][1]]:
        heapq.heappop(maxheap)

    if not minheap or not maxheap:
        return [0, 0]
    return [-maxheap[0][0], minheap[0][0]]
