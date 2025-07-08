def solution(dartResult):
    answer = 0
    before = 0
    digit = 0
    for inx,i in enumerate(dartResult):

        if(i == "1" and dartResult[inx+1] == "0"):
            answer += before
            before = digit
            digit = 10
        elif(inx>0 and dartResult[inx - 1].isdigit() and i.isdigit()):
            continue
        elif(i.isdigit()):
            answer += before
            before = digit
            digit = int(i)

        if(i == "S"):
            digit = digit
        if(i == "D"):
            digit = digit*digit
        elif(i == "T"):
            digit =digit* digit*digit
        elif(i == "*"):
            before = before*2
            digit = digit*2

        elif(i == "#"):
            digit = -digit


    answer = answer + before + digit


    return answer

solution("1D2S#10S")