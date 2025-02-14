from collections import deque

def solution(begin, target, words):

    words.append(begin)
    visited = [False]*(len(words))

    def connectedList(tar):

        reList = []

        for index, n in enumerate(words):
            onedif = 0
            if(n == tar):
                reList.append(1)
            else:
                for a in range(len(tar)):

                    if(tar[a] != n[a]):
                        onedif = onedif+1
                    if(onedif > 1):
                        reList.append(0)
                        break
                    if(a+1 == len(tar) and onedif == 1):
                        reList.append(1)

            
        
        return reList
    
    graph = []
    for i in words:
        graph.append(connectedList(i))

    def bfs(begin):

        a = words.index(begin)
        visited[a] = True
        queue = deque()
        cnt = 0
        queue.append((graph[a],cnt))

        answer = 0

        while(queue):
            v,cnt = queue.popleft()
            for index, i in enumerate(v):
                if(i == 1 and visited[index] == False):
                    if(words[index] == target):
                        answer = cnt + 1
                        queue = []
                        break
                    queue.append((graph[index],cnt + 1))
                    visited[index] = True

        return answer


    return bfs(begin)

solution("hit","hog",["hot", "dot", "hog", "lot", "log", "cog"])