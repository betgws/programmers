def solution(numbers):
    answer = [-1]*len(numbers)
    stack = []

    for index, i in enumerate(numbers):

    
        while(stack and stack[-1][0] < i):
            a, ind = stack.pop()
            answer[ind] = i

        
        stack.append((i, index))

    

    return answer


solution([9, 1, 5, 3, 6, 2])