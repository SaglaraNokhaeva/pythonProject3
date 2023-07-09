# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать «больше» или «меньше» после каждой попытки.
# Для генерации случайного числа используйте код:

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1001
count = 10

num = randint(LOWER_LIMIT, UPPER_LIMIT)
#print(num)

while count > 0:
    print('Попытка № ', count)
    count -= 1

    attempt = float(input('Угадайте число между ' + str(LOWER_LIMIT) + ' и ' + str(UPPER_LIMIT) + ': '))
    if attempt < num:
        print('Больше')
    elif attempt > num:
        print('Меньше')
    else:
        break
else:
    print('Исчерпаны все попытки. Сожалею.')
    quit()
print('Вы угадали! Поздравляем!')
