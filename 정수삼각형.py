def solution(triangle):
    n = len(triangle)
    dp = [[0] * n for _ in range(n)]

    # DP의 마지막 행을 초기값으로 설정
    for i in range(n):
        dp[n-1][i] = triangle[n-1][i]

    # 아래에서 위로 올라가면서 최댓값을 저장
    for i in range(n-2, -1, -1):
        for j in range(i+1):
            dp[i][j] = triangle[i][j] + max(dp[i+1][j], dp[i+1][j+1])

    return dp[0][0]