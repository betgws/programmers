def solution(distance, rocks, n):
    answer = 0
    left = 0
    right = distance

    rocks.append(distance)
    rocks.sort()

    while(left < right):
        mid = (left + right) // 2 
        prev = 0
        remove = 0
        for rock in rocks:
            if(rock - prev < mid):
                remove += 1

            else:
                prev = rock
        if(remove > n):
            right = mid -1 

        else:
            answer = mid
            left = mid + 1 

    return answer