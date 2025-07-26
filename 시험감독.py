N = map(int, input().split())
A = list(map(int, input().split()))
B , C = map(int, input().split())

need = 0
for i in A:
    remain = i - B
    need += 1

    if(remain > 0):
        need += (remain // C)
        if(remain % C > 0):
            need +=1


print(need)


