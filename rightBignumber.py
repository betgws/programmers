n = int(input())
ans = [0]*n
A = list(map(int,input().split()))
mystack = []

for i in range(n):
    while mystack and A[mystack[-1]]< A[i]:
        ans[mystack.pop()] = A[i]
    mystack.append(i)

while mystack:
    ans[mystack.pop()] = -1

result = ""

for i in range(n):
    result += str(ans[i])+' '

print(result)