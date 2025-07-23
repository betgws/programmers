def solution(diffs, times, limit):
    left = 1
    right = max(diffs)
    answer = right # 초기화

    while left <= right:
        mid = (left + right) // 2
        time = 0

        # 주어진 mid 난이도에서 소요 시간 계산
        for i in range(len(diffs)):
            if diffs[i] <= mid:
                time += times[i]
            else:
                g = diffs[i] - mid
                if i != 0:
                    time += (times[i-1] + times[i]) * g + times[i]
                else:
                    time += times[i] * g + times[i]

        # 이분 탐색 조건 (루프 밖에서 판정)
        if time <= limit:
            answer = mid
            right = mid - 1  # 더 작은 난이도로도 가능한지 탐색
        else:
            left = mid + 1   # 난이도를 더 높여야 시간 단축 가능

    return answer



