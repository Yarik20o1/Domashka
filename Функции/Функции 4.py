def time_day(sec):
    day = sec // (24 * 3600)
    hour = (sec - (day * (24 * 3600))) // (24*60)
    minutes = (sec - (day*(24 * 3600) + hour*60)) // 60
    secs = sec - (day*24*3600 + hour*24*60 + minutes*60)
    return f'Дней-{day},часов-{hour},минут-{minutes},секунд-{secs}'


print(time_day(int(input("Введите секунды:"))))
