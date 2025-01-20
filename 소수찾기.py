from itertools import permutations
from itertools import combinations
import itertools

def solution(numbers):

    numList = []
    comList = []
    perList = []
    anList = []

    answer = 0

    for i in numbers:
        numList.append(int(i))

    for i in range(len(numbers)):
        comList.extend(itertools.combinations(numbers, i+1))
    
    for i in comList:
        perList.extend(itertools.permutations(i))

    for i in perList:

        result = int(''.join(map(str, i)))
        anList.append(result)


    anList = set(anList)


    for i in anList:
        if(is_prime(i)):
            answer = answer + 1

    return answer


def is_prime(number):
    if number <= 1:  # 1 이하의 숫자는 소수가 아님
        return False
    if number == 2:  # 2는 소수
        return True
    if number % 2 == 0:  # 짝수는 소수가 아님
        return False
    
    # 3부터 제곱근까지 확인
    for i in range(3, int(number**0.5) + 1, 2):
        if number % i == 0:
            return False
    return True


solution("011")