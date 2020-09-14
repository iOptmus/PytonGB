"""
2.
Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
"""
while True:
    time_sec = input('Введите время в секундах:\n')
    if time_sec.isdigit():
        break
    print('введите число секунд!')

time_sec = int(time_sec)
hour_time = time_sec//3200
minute_time = time_sec%3200//60
second_time = time_sec%3200%60
print(f"{hour_time:>02} : {minute_time:>02} : {second_time:>02}")
