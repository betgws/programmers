import math

def solution(r1, r2):
  answer = 0
  c1 = findDotNumber(r1)
  c2 = findDotNumber(r2)

  answer = c2 -c1 +4 
  return answer

def findDotNumber(r):
  x = 0
  y = 0 
  answer = 0
  count = 0

  for xx in range(r+1):
      
      rargeY = r*r - xx*xx
      yy = int(math.sqrt(rargeY))

      count += yy + 1 

      print(count)

  print(answer*4 - (r+1)*4)

  return count*4 - r*4 + 1

solution(2,3)