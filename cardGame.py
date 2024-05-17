from collections import deque

n = int(input())
a = deque()

for i in range(1, n+1):
    a.append(i)

while len(a)>1:
    a.popleft()
    a.append(a.popleft)

print(a[0])


    
