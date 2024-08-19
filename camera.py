def solution(routes):
    
    sortedList = sorted(routes, key=lambda x: x[0])
    
    #초기 세팅
    stack = []
    stack.append(sortedList[0])
    answer = 1
    a = sortedList[1][1]
    
    for i in sortedList[1:]:
        if stack[-1][1] - i[0] >= 0:
            if a - i[0] >= 0:
                stack.pop()
                stack.append(i)
            elif a - i[0] < 0:
                a = i[1]
                stack.append(i)
                answer = 1 + answer
        else:
            stack.pop()
            a = i[1]
            stack.append(i)
            answer = 1+ answer
        
    
    
    return answer

def main():
    print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]))
    