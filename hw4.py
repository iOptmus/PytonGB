"""
Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.
"""
while True:
    number = input('Введите число:\n')
    if number.isdigit():
        number = int(number)
        break
    print('Необходимо ввести число!')
max_digit = number % 10
while number:
    number //= 10
    temp_digit = number % 10
    if temp_digit == 9:
        max_digit = temp_digit
        break
    if temp_digit > max_digit:
        max_digit = temp_digit
print(f'Максимальная цифра в числе: {max_digit}')
