def solve():
    import sys
    input = sys.stdin.readline

    N = int(input().strip())

     # 1일부터 N일까지 쓸 수 있도록 1-based 배열로 초기화
    T = [0] * (N + 1)
    P = [0] * (N + 1)
    for i in range(1, N + 1):
        T[i], P[i] = map(int, input().split())


    dp = [0] * (N+2)


    for i in range(N,0,-1):
        if i + T[i] <= N +1:
            dp[i] = max(P[i] + dp[i+T[i]], dp[i+1]) 

        else:
            dp[i] = dp[i+1]

    print(dp[1])