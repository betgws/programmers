def solution(n,times):
    left = 1
    right = max(times)*n

    answer = right 

    while(left <= right):
        mid = (left+right//2)
        total = sum(mid// f for f in times)

        if(total >= n):
            answer = mid
            right = mid - 1

        else: 
            left = mid+1 


    return answer 






