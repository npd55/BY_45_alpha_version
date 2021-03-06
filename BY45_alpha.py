import math

# импорт модуля math для математических операций


hello_msg = ('Привет! Я Альфа версия программы для расчета справки ВУ-14, для'
             ' грузового состава 4-х осных вагонов.\n'
             'Пока я умею только считать по данным что вы мне передаете,'
             ' но в будущем\n'
             'я обзаведусь искусственным интеллектом и машинным зрением;)\n'
             'И вам будет достаточно отправить фото с данными состава,'
             ' а я все сделаю сама.\n'
             'Но пока посчитаем по простому, нанчем?)')
# просто приветственное сообщение с небольшим анонсом будущих возможностей

print(hello_msg)
# вывод приветственного сообщения

'''Ввод данных'''
try:
    weight = int(input("Введите вес состава: "))
    # получение веса состава
    pressing = int(input("Введите нажатие (33, 44, 55) тс: "))
    # получение нажатия
    axis = int(input("Количество осей: "))
    # получение количества осей
    laden = int(input("Количесто груженых: "))
    # получение количества груженых вагонов
    empty = int(input("Количество порожних: "))
    # получение количества порожних вагонов
except ValueError:
    print('Ошибка ввода! Пожалуйста, вводите числовые значения')


'''Расчет потребного нажатия в зависимости от типа состава'''
if pressing == 33:
    necessary = math.ceil(weight * 0.33)
elif pressing == 44:
    necessary = math.ceil(weight * 0.44)
else:
    necessary = math.ceil(weight * 0.55)
# расчет потребного нажатия

'''Считаем количество осей порожних/груженых вагонов'''
empty_axis = 4 * empty
#
laden_axis = 4 * laden
#

'''Считаем фактическое нажатие у порожних/груженых вагонов'''
necessary_empty = empty_axis * 3.5
necessary_laden = laden_axis * 7

if laden == 0:
    necessary_fact = empty_axis * 3.5
elif empty == 0:
    necessary_fact = laden_axis * 7
else:
    necessary_fact = necessary_laden + necessary_empty


manual = math.ceil(weight * 0.4 / 100)
# расчет потребного количества ручных томрозов в осях

print('Потребное нажатие: ' + str(necessary) + ' тс')
print('Ручных тормозов в осях: ' + str(manual))
print('Количество осей порожних вагонов: ' + str(empty_axis) + ' Нажатие: '
      + str(necessary_empty) + ' тс')
print('Количество осей груженых вагонов: ' + str(laden_axis) + ' Нажатие: '
      + str(necessary_laden) + ' тс')
print('Фактическое нажатие: ' + str(necessary_fact) + ' тс')
