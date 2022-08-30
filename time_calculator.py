def add_time(begin, additional_time, day=None):
    begin, part = begin.split()
    begin = begin.split(':')
    additional_time = additional_time.split(':')

    week = {'Monday': 0,
            'Tuesday': 1,
            'Wednesday': 2,
            'Thursday': 3,
            'Friday': 4,
            'Saturday': 5,
            'Sunday': 6}
    week_reverse = {}
    for key, value in week.items():
        week_reverse[value] = key

    part_of_day = {'AM': 1, 'PM': 0}
    part_of_day_reverse = {'1': 'AM', '0': 'PM'}
    third = str()
    first_int, second_int, days = int(), int(), int()
    first_int += int(begin[0]) + int(additional_time[0])
    second_int = int(begin[1]) + int(additional_time[1])

    if second_int >= 60:
        first_int += second_int // 60
        second_int = second_int % 60
    if second_int < 10:
        second_int = '0' + str(second_int)
    if first_int >= 12:
        print(part)
        if part_of_day[part] == 1:
            part = part_of_day_reverse[str((part_of_day[part] + first_int // 12) % 2)]
            days += first_int // 24

        else:
            days += 1
            part = part_of_day_reverse[str((part_of_day[part] + first_int // 12) % 2)]
            days += first_int // 24

        first_int = first_int % 12
        if first_int == 0:
            first_int = 12

    if days:
        if days == 1:
            third += f' (next day)'
        else:
            third += f' ({days} days later)'

    if day:
        day = day.lower()
        day = day[0].upper() + day[1:]
        number = week[day]
        day = week_reverse[(number + days) % 7]
        return f'{first_int}:{second_int} {part}, {day}{third}'
    else:
        return f'{first_int}:{second_int} {part}{third}'
