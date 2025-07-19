import heapq

def solution(operations):
    minheap = []
    maxheap = []

    for op in operations:
        cmd, num = op.split()
        num = int(num)

        if cmd == 'I':  # 값 삽입
            heapq.heappush(minheap, num)
            heapq.heappush(maxheap, -num)  # 최대힙은 음수로
        elif cmd == 'D':
            if num == 1 and maxheap:  # 최대값 삭제
                max_val = -heapq.heappop(maxheap)
                minheap.remove(max_val)  # 다른 힙에서도 제거
                heapq.heapify(minheap)   # 힙 재정렬
            elif num == -1 and minheap:  # 최소값 삭제
                min_val = heapq.heappop(minheap)
                maxheap.remove(-min_val)
                heapq.heapify(maxheap)

    # 결과 계산
    if not minheap:
        return [0, 0]
    return [max(minheap), min(minheap)]
