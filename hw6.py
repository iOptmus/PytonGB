"""
6. Спортсмен занимается ежедневными пробежками.
В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.

Например: a = 2, b = 3.

Результат:

1-й день: 2
2-й день: 2,2
3-й день: 2,42
4-й день: 2,66
5-й день: 2,93
6-й день: 3,22
Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.
"""
start_distance = int(input('Введите результат 1-й пробежки: \n'))
finish_distance = int(input('Введите итоговый результат пробежки: \n'))
day_count = 1
while finish_distance > start_distance:
#    print('{}-й день: {:.2f}'.format(day_count, start_distance))
    start_distance *= 1.1
    day_count += 1
    print(f'{day_count}-й день: {start_distance:.2f}')
#    if start_distance > finish_distance:
print(f'Ответ: на {day_count}-й день спортсмен достиг результата — не менее {finish_distance} км.')
