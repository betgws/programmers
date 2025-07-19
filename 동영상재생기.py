def solution(video_len, pos, op_start, op_end, commands):
    

    video_len = hToM(video_len)
    pos = hToM(pos)
    op_start = hToM(op_start)
    op_end = hToM(op_end)

    answer = pos

    for i in commands:
        if i == "next":
            if op_start <= pos + 10 <= op_end or op_start <= pos  <= op_end :
                answer = op_end
            elif pos + 10 >= video_len:
                answer = video_len
            else: 
                answer = answer + 10  

        if i == "prev":
            if answer < 10:
                answer = 0
            else:
                answer = answer - 10

    hour = answer//60
    minute = answer % 60

    hourStr = str(hour)
    minuteStr = str(minute)

    if len(hourStr) < 2:
        hourStr = "0"+hourStr
    if len(minuteStr) < 2:
        
            
    
    return hourStr+":"+minuteStr

def hToM(video):
    hourStr, minuteStr = video.split(":")
    hour = int(hourStr)
    minute = int(minuteStr)
    hour = hour*60
    total = hour + minute

    return total

solution("10:55", "00:05", "00:15", "06:55", ["prev", "next", "next"])
