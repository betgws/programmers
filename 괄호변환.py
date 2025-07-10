from collections import deque

def solution(p):
    if not p:
        return ""

    u, v = divide(p)

    if isGood(u):
        return u + solution(v)
    else:
        return "(" + solution(v) + ")" + reverse(u[1:-1])

def divide(string):
    left = 0
    right = 0
    for i in range(len(string)):
        if string[i] == '(':
            left += 1
        else:
            right += 1
        if left == right:
            return string[:i+1], string[i+1:]

def isGood(string):
    stack = deque()
    for ch in string:
        if ch == '(':
            stack.append(ch)
        else:
            if not stack:
                return False
            stack.pop()
    return not stack

def reverse(s):
    result = ""
    for ch in s:
        result += ')' if ch == '(' else '('
    return result
