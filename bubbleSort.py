n = int(input())
A=[0]*n

for i in range(n):
    A[i] = int(input())

for i in range(n-1):
    for j in range(n-1-i):
        if A[j]>A[1+j]:
            temp = A[j+1]
            A[j+1] = A[j]
            A[j] = temp

for i in range(n):
    print(A[i])
