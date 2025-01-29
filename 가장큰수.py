
def solution(numbers):

    sorted_data = sorted(map(str,numbers))
    Temp = []
    answer = ""

    while(sorted_data or Temp):

        if(sorted_data):
            a = sorted_data.pop()
            if(len(a) == 1):
                answer = answer + a
            elif(len(a) > 1 and a[1]>a[0]):
                answer = answer + a

            else:
                Temp.append(a)
                if(sorted_data):
                    i = sorted_data.pop()
                    while(i[0] == a[0]):
                        if(len(i) == 1):
                            answer = answer + i
                        else:
                            Temp.append(i)
                        if(sorted_data):
                            i = sorted_data.pop()
                        else: i =" "

                Temp.sort()
                while(Temp):
                    answer = answer + Temp.pop()
                    
            
                
    return answer

solution([32, 322, 5,7,3])

