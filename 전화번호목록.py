def solution(phone_book):

    phone_book.sort(key = len)

    temp = [phone_book[0]]
    
    for i in range(1, len(phone_book)):
        for a in temp:
            if a == phone_book[i][:len(a)]:
                return False
        temp.append(phone_book[i])
        
    return True


solution(["119", "97674223", "1195524421"])