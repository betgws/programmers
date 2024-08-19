from collections import deque

def solution(tickets):

    answer = []

    tickets.sort(key = lambda x : (x[0],x[1]))

    dq = deque((["ICN"],tickets))

    while dq:

        nowPath, nowTickets = dq.popleft()

        if len(nowTickets) == 0:
            answer = nowPath
            break

        valid_idx = -1
        for i in range(len(nowTickets)):
            if nowTickets[i][0] == nowPath[-1]:
                valid_idx = i

        if valid_idx == -1:
            continue

        while valid_idx < len(now_t) and now_t[valid_idx][0] == now_path[-1]:
            dq.append((now_path + [now_t[valid_idx][1]], now_t[:valid_idx] + now_t[valid_idx+1:]))
            
            valid_idx += 1

    return answer