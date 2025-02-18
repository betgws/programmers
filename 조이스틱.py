from collections import defaultdict

def solution(name):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    dic = defaultdict(int)

    # 알파벳 조작 횟수 설정 (A에서 최단 거리 이동)
    for i in range(len(alphabet)):
        dic[alphabet[i]] = min(i, 26 - i)  # 위로 이동 vs 아래로 이동 최솟값

    name = list(name)

    move = len(name) - 1  # 초기 좌우 이동 최댓값

    total_moves = 0
    for i, char in enumerate(name):
        total_moves += dic[char]  # 알파벳 조작 횟수 추가

        # 🔹 `A`가 연속되는 부분을 찾아서 `next_index` 결정 (최적 이동 찾기)
        next_index = i + 1
        while next_index < len(name) and name[next_index] == "A":
            next_index += 1

        # 🔥 최적의 커서 이동 경로 선택
        move = min(move, (i * 2) + (len(name) - next_index))
        move = min(move, (len(name) - next_index) * 2 + i)

    return total_moves + move
solution("JAAJAAAAJ")