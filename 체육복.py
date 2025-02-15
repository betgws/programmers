def solution(n, lost, reserve):

    lost.sort()
    lost1 = lost.copy()

    for i in lost1:
        if(i in reserve):
            lost.remove(i)
            reserve.remove(i)

    lost2 = lost.copy()

    for i in lost2:
        
        if(i-1 in reserve):
            lost.remove(i)
            reserve.remove(i-1)
            

        elif(i+1 in reserve):
            lost.remove(i)
            reserve.remove(i+1)

    
    return  n - len(lost)


solution( 5, [4, 2], [3, 5])