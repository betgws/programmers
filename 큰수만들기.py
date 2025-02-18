def solution(number, k):
    stack = []  # 결과를 저장할 스택

    for num in number:  # 숫자를 순서대로 탐색 (O(n))
        while stack and k > 0 and stack[-1] < num:  # 스택에서 작은 숫자 제거 (최대 O(n))
            stack.pop()  
            k -= 1
        stack.append(num)  # 현재 숫자를 스택에 추가 (O(1))

    return "".join(stack[:len(number) - k])  # 필요한 개수만큼 반환 (O(n))
