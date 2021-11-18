user_input = input("Введите, пожалуйста, номер месяца: ")
month = int(user_input)
print('Вы ввели ,', month)
if month == 1:
    print("В январе 31 день")
if month == 2:
    print("В феврале 28 дней")
if month == 3:
    print("В марте 31 день")
if month == 4:
    print("В апреле 30 день")
if month == 5:
    print("В мае 31 день")
if month == 6:
    print("В июне 30 день")
if month == 7:
    print("В июле 31 день")
if month == 8:
    print("В августе 30 день")
if month == 9:
    print("В сентябре 31 день")
if month == 10:
    print("В октября 30 день")
if month == 11:
    print("В ноябре 31 день")
if month == 12:
    print("В декабре 31 день")
else:
    print('Номер месяца не коректный')
