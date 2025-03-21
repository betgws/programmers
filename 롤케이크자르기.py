def solution(topping):
    answer = 0
    intopping = []
    rTopping = [0]*len(topping)
    lTopping = [0] *len(topping)
    now = 0

    for index, i in enumerate(topping):
        if(i not in intopping):
            intopping.append(i)
            rTopping[index] = now + 1
            now = now + 1
        else:
            rTopping[index] = now

    intopping = []
    now = 0
    for index in range(len(topping) - 1, -1, -1):
        if(topping[index] not in intopping ):
            intopping.append(topping[index])
            lTopping[index] = now + 1
            now = now +1

        else:
            lTopping[index] = now

    

    for index, i in enumerate(rTopping):
        if(index+1 != len(topping) and i == lTopping[index+1]):
            answer = answer + 1

        else:
            continue



    return answer

solution([1, 2, 3, 1, 4])