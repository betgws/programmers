n = 4

ans = 0
row = [0] * n

def is_promising(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    
    return True

def n_queens(x):
    global ans
    if x == n:
        ans += 1
        return

    else:
        for i in range(n):
            # [x, i]에 퀸을 놓겠다.
            row[x] = i
            if is_promising(x):
                n_queens(x+1)

n_queens(0)
print(ans)


ans = 0
n = 3
row = [0]*n


def n_queen(x):

    for i in range(n):
        row[x] = i
        if is_promissing(x):
            n_queen(x+1)


def is_promissing(x):
    for i in range(x):
        if(row[x] == row [i] and abs(row[x] - row[i]) == abs(x-i)):
            return False
    return True
