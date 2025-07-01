def solution(new_id):
    answer = ''
    
    # 1단계: 소문자로 치환
    new_id = new_id.lower()

    # 2단계: 허용된 문자만 남기기
    for ch in new_id:
        if ('a' <= ch <= 'z') or ch.isdigit() or ch in ['-', '_', '.']:
            answer += ch

    # 3단계: 연속된 마침표를 하나로
    temp = ''
    for ch in answer:
        if not (temp and temp[-1] == '.' and ch == '.'):
            temp += ch
    answer = temp

    # 4단계: 처음이나 끝의 마침표 제거
    if answer and answer[0] == '.':
        answer = answer[1:]
    if answer and answer[-1] == '.':
        answer = answer[:-1]

    # 5단계: 빈 문자열이면 'a'
    if answer == '':
        answer = 'a'

    # 6단계: 길이 16자 이상이면 자르고, 끝에 . 있으면 제거
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]

    # 7단계: 길이 2자 이하면 마지막 문자 반복
    while len(answer) < 3:
        answer += answer[-1]

    return answer
