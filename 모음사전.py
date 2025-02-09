def solution(word):
    answer = 0
    dictionary = []  # 가능한 단어들을 저장할 리스트
    words = 'AEIOU'  # 사용할 문자 리스트

    def dfs(cnt, w):  # DFS 탐색 함수
        # 최대 길이는 5
        if cnt == 5:
            return
        
        for i in range(len(words)):  # 'A', 'E', 'I', 'O', 'U' 중 하나 추가
    
            dictionary.append(w + words[i])  # 새로운 단어 생성 후 리스트에 추가
            dfs(cnt + 1,  w + words[i])  # 재귀 호출하여 다음 문자 추가

    dfs(0, '')  # DFS 탐색 시작 (초기값: 길이 0, 빈 문자열)
    
    return dictionary.index(word) + 1  # 리스트에서 단어의 위치 찾기 (1-based index)


solution("AAAAE")

def solution(word):
    str = "AOUEB"
    dic = []
    w = ""
    cnt =0

    def dfs(cnt,w):
        if cnt == 5:
            return
        for i in str:
            dic.append(w+str[i])
            dfs(cnt+1,w+str[i])
