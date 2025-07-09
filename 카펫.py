




def solution(brown,yellow):
    answer = []

    for vertical in range((yellow//2)):
        vertical = vertical + 1
        if(yellow%vertical != 0):
            continue
        horizontal = int(yellow/vertical)

        if(vertical*2 + horizontal*2 + 4 == brown):
            return [horizontal+2,vertical+2]
        

    
solution(8,1)










