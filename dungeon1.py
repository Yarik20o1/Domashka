import json

with open('rpg.json', 'r') as f1:
    data = json.load(f1)
    print(data)
remaining_time = '1234567890.0987654321'
while True:
    n = input('Выберите действие:\n'
              '1.Атаковать монстра \n'
              '2.Перейти в другую локацию\n'
              '3.Выход')
    print(
        f'Вы находитесь в {1}\n'
        f'У вас {1} опыта и осталось {remaining_time} секунд\n'
        f'Прошло уже {1}\n'
        f'Внутри вы видите:\n'
        f'-- Монстра {1}\n'
        f'-- Вход в локацию: {1}\n'
        f'-- Вход в локацию: {1}')
