
def solution(citations):
    citations.sort(reverse=True)  # 내림차순 정렬
    h_index = 0

    for i, citation in enumerate(citations):
        if citation >= i + 1:  # 현재 논문의 인용 횟수가 (현재 논문 순위 이상)일 때
            h_index = i + 1  # H-Index 업데이트
        else:
            break  # 더 이상 조건을 만족하지 않으면 종료
    
    return h_index

solution([4, 0, 6, 1, 5])