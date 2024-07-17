def solution(operations):
    answer = [] 
    minheap = []
    maxheap = []
    minRemove = 0
    
    for i in operations:
        a = i.split(' ')
        
        if(a[0] == 'I'):
            heapq.heappush(minheap, int(a[1]))
            heapq.heappush(maxheap, int(-a[1]))
            
        elif(a[0] == "D"):
            if(a[1] == '-1'):
                if(max >= len(minheap)):
                    minheap = []
                    maxheap = []
                    max = 0
                    min = 0
                minheap.pop()
                min += 1
                
            elif (a[1] == "1"):
                if(min >= len(maxheap)):
                    maxheap=[]
                    minheap = []
                    min = 0
                    max = 0
                maxheap.pop()
                max += 1
                
    if(max >= len(minheap) or min >= len(maxheap)):
        return [0,0]
    answer.append[minheap.pop(), -maxheap.pop()]
    print(answer)
                
            
    return answer

def main():
    oper = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
    a = solution(oper)
    print(a)
    