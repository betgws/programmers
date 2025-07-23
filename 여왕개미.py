totalCommands = 0
anthillDeleted = [False]       # 각 개미집이 철거되었는지 표시
anthillPositions = [0]         # 개미집 좌표 (0번은 여왕 개미 집)

def initialVillageConstruction(input_array):
    numInitialAnthills = input_array[0]
    for i in range(1, numInitialAnthills + 1):
        position = input_array[i]
        anthillPositions.append(position)
        anthillDeleted.append(False)

def addNewAnthill(input_array):
    newAnthillPosition = input_array[0]
    anthillPositions.append(newAnthillPosition)
    anthillDeleted.append(False)

def removeAnthill(input_array):
    anthillNumber = input_array[0]
    anthillDeleted[anthillNumber] = True

def processScoutQuery(input_array):
    numAnts = input_array[0]
    lowerBound, upperBound = 0, 1000000000
    minimumTime = 0

    # 이진 탐색으로 최소 시간 T 찾기
    while lowerBound <= upperBound:
        midTime = (lowerBound + upperBound) // 2
        intervalsNeeded = 0
        lastCoveredPosition = -1000000000

        # 살아있는 개미집들만 확인하며 구간 개수 계산
        for i in range(1, len(anthillPositions)):
            if anthillDeleted[i]:
                continue
            currentAnthillPosition = anthillPositions[i]
            if currentAnthillPosition - lastCoveredPosition > midTime:
                lastCoveredPosition = currentAnthillPosition
                intervalsNeeded += 1

        # 개미 수로 커버 가능한지 확인 후 범위 조정
        if intervalsNeeded <= numAnts:
            minimumTime = midTime
            upperBound = midTime - 1
        else:
            lowerBound = midTime + 1

    print(minimumTime)

# 명령어 입력 및 처리
totalCommands = int(input())
while totalCommands:
    totalCommands -= 1
    input_array = list(map(int, input().split())) 
    commandType = input_array[0]
    
    if commandType == 100:
        initialVillageConstruction(input_array[1:])
    elif commandType == 200:
        addNewAnthill(input_array[1:])
    elif commandType == 300:
        removeAnthill(input_array[1:])
    elif commandType == 400:
        processScoutQuery(input_array[1:])
