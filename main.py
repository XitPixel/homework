# 1.С помощью функции map выведите список имен с заглавной буквы.
# names = ['alfred', 'tabitha', 'william', 'arla']
# Результат: ['Alfred', 'Tabitha', 'William', 'Arla']

# names = ['alfred', 'tabitha', 'william', 'arla']
#
# def up(item):
#     return item.title()
#
# names2 = list(map(up, names))
# print(names2)

# 2.С помощью функции filter выведите список оценок, которые больше 75.
# scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
# Результат: [90, 76, 88, 81]

# scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
#
# def more75(item):
#     return item > 75
#
# scores2 = list(filter(more75, scores))
# print(scores2)

# 3.Сначала используйте функцию, объявленную с помощью def,
# С помощью функции filter выведите список слов-палиндромов.
# words = ['Anna', 'Alexey', 'Alla', 'Kazak', 'Dom']
# Результат: ['Anna', 'Alla', 'Kazak']

# words = ['Anna', 'Alexey', 'Alla', 'Kazak', 'Dom']
#
# def poli(item):
#     return item[::-1].lower() == item.lower()
#
# word2 = list(filter(poli, words))
# print(word2)

# 4.Есть список слов. Нужно с помощью map  вернуть список длин этих слов.
#  ('apple', 'banana', 'cherry')
# Результат: [5, 6, 6]

# fruit = ['apple', 'banana', 'cherry']
#
# print(list(map(len, fruit)))

# Уровень: Стандартный

# 1.Есть два текстовых списка. Нужно вернуть один список объединенных слов.
# Подаваемые данные: 2 списка
# ['apple', 'banana', 'cherry'], ['orange', 'lemon', 'pineapple']
# Результат:
# ['appleorange', 'bananalemon', 'cherrypineapple']

# one = ['apple', 'banana', 'cherry']
# two = ['orange', 'lemon', 'pineapple']
#
# three = list(map(lambda x, y: x + y, one, two))
# print(three)

# Уровень: Продвинутый

# import time
#
# n = int(input('Введите число: '))
# s = time.time()
# lst = [i for i in range(int(n))]
# f = time.time()
#
# print(f - s)