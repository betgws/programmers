def solution(book_time):



    converted_times = [[time_to_minutes(start), time_to_minutes(end)+10] for start, end in book_time]
    converted_times.sort(key=lambda x: x[0])

    hotel = []

    for i in converted_times:
        if not hotel:
            hotel.append(i)
            continue
        for index, room in enumerate(hotel):
            if i[0] >= room[-1]:
                hotel[index] = room + i
                break

        else:
            hotel.append(i)

    



    
    return len(hotel)


def time_to_minutes(time_str):
    hours, minutes = map(int, time_str.split(':'))
    return hours * 60 + minutes