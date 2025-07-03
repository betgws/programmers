import math

def solution(fees, records):
    answer = []
    set1 = set()
    inOut = {}
    costDic = {}

    # cost 계산하는 함수
    def costCalculate(start, end):
        startHour, startMinute = map(int, start.split(":"))
        endHour, endMinute = map(int, end.split(":"))

        start = startHour*60 + startMinute
        end = endHour*60 + endMinute

        usingTime = end - start

        if(usingTime <= fees[0]):
            return fees[1]
        
        else:
            return fees[1] + (math.ceil((usingTime-fees[0])/fees[2]))*fees[3]
            

    #딕셔너리 초기화 
    for i in records:
        clock, number, kind = i.split()
        set1.add(number)

    sortedList = sorted(set1)

    for i in sortedList:
        inOut[i] = []
        costDic[i] = 0

    #딕셔너리 만들면서 동시에 len==2면 주차요금 계산 
    for i in records:
        clock, number, kind = i.split()
        inOut[number].append(clock)

        if(len(inOut[number])==2):
            cost = costCalculate(inOut[number][0], inOut[number][1])
            costDic[number] += cost
    
    for i in inOut.keys:
        if(inOut[i]):
            cost = costCalculate(inOut[i][0], "23:59")
            costDic[i] += cost

    
    for i in costDic:
        answer.append(costDic[i])
            



        
    return answer

solution([180, 5000, 10, 600],["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"])