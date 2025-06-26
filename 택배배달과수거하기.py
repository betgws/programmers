def solution(cap, n, deliveries, pickups):
    answer = 0

    deliver = n - 1
    get = n - 1

    # 첫 시작점 찾기
    while deliveries[deliver] == 0:
        deliver = deliver - 1
    while pickups[get] == 0:
        get = get - 1 

    total = sum(deliveries) + sum(pickups)
    
    while total:
        answer = answer + (max(deliver,get) + 1)*2

        deliverCap = cap
        getCap = cap

        while(deliver >= 0 and deliveries[deliver] <= deliverCap):
            
            total = total - deliveries[deliver]
            deliverCap = deliverCap - deliveries[deliver]
            deliveries[deliver] = 0
            deliver = deliver - 1 

        while(get >= 0 and pickups[get] <= getCap):
            total = total - pickups[get]
            getCap = getCap - pickups[get]
            pickups[get] = 0
            get = get - 1

        if(deliver > 0 and deliveries[deliver] > deliverCap):
            deliveries[deliver] = deliveries[deliver] - deliverCap
            total = total - deliverCap
            deliverCap = 0

        if(get> 0 and pickups[get] > getCap):
            pickups[get] = pickups[get] - getCap
            total = total - getCap
            getCap = 0
        
        
    return answer

solution(2,7,[1, 0, 2, 0, 1, 0, 2],[0, 2, 0, 1, 0, 2, 0])