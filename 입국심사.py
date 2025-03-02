def solution(n, times):
	
    left = 1
    right = max(times) * n
    
    # 이분탐색이니 left가 right 이하인 동안
    while left <= right:
    	# 가운데 : 더하고 2로 나눈 몫(정수)
        mid = (left+right)//2
        # 심사한 사람 수
        people = 0
     	
        for time in times:
        	# 해당 심사대에서 주어진 시간동안 심사 받은 수 더하기
            people += mid//time
            
            # 중간에라도 이미 n명보다 많이 심사했다면 break
            if people >= n:
                break
     
        if people >= n:
            answer = mid
            right = mid -1
     
        else :
            left = mid + 1
    return answer

solution(6,[7, 10000000])