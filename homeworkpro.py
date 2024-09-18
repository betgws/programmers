from collections import deque

def solution(plans):
    
    for sublist in plans:
        
        # 시간 문자열을 시간과 분으로 분리하여 정수로 변환
        time_str = sublist[1]
        hour, minute = map(int, time_str.split(':'))
        # 필요에 따라 시간 값을 분으로 변환하거나 datetime 객체로 변환 가능
        total_minutes = hour * 60 + minute
        sublist[1] = total_minutes  # 또는 (hour, minute) 튜플로 저장 가능
        # 문자열로 된 숫자를 정수로 변환
        sublist[2] = int(sublist[2])

    sortedPlan = deque(sorted(plans, key=lambda x:x[1]))
    notComplete= deque()
    complete = deque()
    now = sortedPlan[0][1]
    i = 0

    while(len(complete) < len(plans)):
        # 아직 soredPlan을 할 시간이 오지 않았고 notComplete가 남아있다면
        if(now < sortedPlan[i][1] and notComplete):
            nowPlan = notComplete.pop()
        else:
            if(now <sortedPlan[i][1] ):
                now = sortedPlan[i][1]
            
            nowPlan = sortedPlan.popleft() 

        # sorted Plan이 비어있다면
        if not sortedPlan:
            complete.append(nowPlan[0])
            for i in range(len(notComplete)):
                complete.append((notComplete.pop())[0])
    
        # 작업 완료되는 시간이 뒤에 나올 작업의 끝내는 시간보다 빠르다면 
        elif(now+nowPlan[2] <= sortedPlan[i][1]):
            complete.append(nowPlan[0])
            now = now + nowPlan[2]

        else:
            nowPlan[2] = nowPlan[2]- (sortedPlan[i][1] - now)
            now = now + (sortedPlan[i][1] - now)
            notComplete.append(nowPlan)   

                 
        
    print(complete)

    return list(complete)


solution([["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]])