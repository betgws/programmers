def solution(users, emoticons):
    answer = [0, 0]
    discountRate = [10, 20, 30, 40]
    discountList = []

    def DFS(tmp, n):
        if n == len(emoticons):
            discountList.append(tmp[:])
            return
        for i in discountRate:
            tmp.append(i)
            DFS(tmp, n + 1)
            tmp.pop()

    DFS([], 0)

    for i in discountList:
        Rpay = 0
        plus = 0
        for user in users:
            pay = 0
            for j in range(len(emoticons)):
                if user[0] <= i[j]:
                    pay += int(emoticons[j] * (100 - i[j]) / 100)  # 정수 처리
            if pay >= user[1]:
                pay = 0
                plus += 1
            Rpay += pay

        if plus > answer[0] or (plus == answer[0] and Rpay > answer[1]):
            answer = [plus, Rpay]

    return answer
