def solution(cap, n, deliveries, pickups):
    answer = 0

    deliver = n - 1
    get = n - 1

    while deliver >= 0 or get >= 0:
        # deliver/get 포인터가 가리키는 유효한 위치 찾기
        while deliver >= 0 and deliveries[deliver] == 0:
            deliver -= 1
        while get >= 0 and pickups[get] == 0:
            get -= 1

        # 종료 조건
        if deliver < 0 and get < 0:
            break

        # 현재 라운드 최대 거리
        distance = max(deliver, get) + 1
        answer += distance * 2

        deliverCap = cap
        getCap = cap

        # 배달 처리
        while deliver >= 0 and deliverCap > 0:
            if deliveries[deliver] <= deliverCap:
                deliverCap -= deliveries[deliver]
                deliveries[deliver] = 0
                deliver -= 1
            else:
                deliveries[deliver] -= deliverCap
                break

        # 수거 처리
        while get >= 0 and getCap > 0:
            if pickups[get] <= getCap:
                getCap -= pickups[get]
                pickups[get] = 0
                get -= 1
            else:
                pickups[get] -= getCap
                break

    return answer

def solution2(cap, n, deliveries, pickups):
    answer = 0
    delivery = 0
    pickup = 0
    
    for i in range(n-1, -1, -1):  # ▶️ 가장 먼 집부터 (역순)
        delivery += deliveries[i]
        pickup += pickups[i]

        while delivery > 0 or pickup > 0:  # ▶️ 한 번 더 가야 하는 경우
            delivery -= cap
            pickup -= cap
            answer += (i + 1) * 2  # ▶️ 왕복 거리 추가
    return answer
        
        


        




solution1(2,7,[1, 0, 2, 0, 1, 0, 2],[0, 2, 0, 1, 0, 2, 0])