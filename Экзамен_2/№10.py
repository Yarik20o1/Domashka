try:
    b = int(input())
    b * (b / 0)
except ZeroDivisionError:
    print('нельзя делить на ноль!')
finally:
    print('Прощай, мир!')
