def solution(diffs, times, limit):
    answer = 0
    
    left = 0
    right = max(diffs)
    answer = 0
    while left <= right:
        mid = left + right // 2
        level = 0

        for i in range(diffs):
            if diffs[i] <= mid:
                

    return answer