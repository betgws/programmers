def solution(m, n, puddles):

    dp = [[0 for _ in range(m+1)]for _ in range(n+1)]

    dp[1][1] = 1
    dp[n][m] = 2

    for i in puddles:
        dp[i[1]][i[0]] = "X"

    for i in range(1,n+1):
        for j in range(1,m+1):

            if((i == 1 and j == 1) or dp[i][j] == "X"):
                continue
            else:
                if(dp[i][j-1] != "X" and dp[i-1][j] != "X"):
                    dp[i][j] = dp[i][j-1] + dp[i-1][j]
                elif(dp[i][j-1] == "X" and dp[i-1][j] != "X"):
                    dp[i][j] = dp[i-1][j] 
                elif(dp[i][j-1] != "X" and dp[i-1][j] == "X"):
                    dp[i][j] = dp[i][j-1]


    return dp[n][m]

solution(4,3,[[2, 2]])