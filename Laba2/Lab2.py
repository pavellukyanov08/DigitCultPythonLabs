# Задание 1
# num1 = int(input('Введите 1 число: '))
# num2 = int(input('Введите 2 число: '))
#
# print(f'Произведение: {num1 * num2}')
#
#
# num1 = int(input('Введите 1 число: '))
# num2 = int(input('Введите 2 число: '))
# num3 = int(input('Введите 3 число: '))
#
# print(f'Сложение первых 2-х и умножение на 3-е: {(num1 + num2) * num3}')


# Задание 2
# string = input('Введите строку: ')
# print(f'Два первых и 2 последних: {string[:2] + string[-2:]}')


# string = input('Введите строку: ')
# print(f'Два первых и 2 последних: {string[:2] + string[-1:]}')


# Задание 3
# year_list = [2002, 2003, 2004, 2005, 2006, 2007]
# print(year_list[3])


# year_list = [2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009]
# print(year_list[4])


# Задание 4
# word = input('Введите слово: ')
# isPalindrome = 'Слово палиндром' if word.lower() == word[::-1] else 'Слово не палиндром'
# print(isPalindrome)


# counter = 0
# while counter < 3:
#     word = input('Введите слово: ')
#     if word.lower() == word[::-1]:
#         counter += 1
#         print('Слово палиндром')
#     else:
#         print('Слово не палиндром')
#         break


# Задание 5
# nums_list = []
# nums = 0
#
# while nums < 4:
#     nums = int(input('Введите число: '))
#     for i in range(nums, nums + 1):
#         nums_list.append(i)
# print(f'Список чисел: {nums_list}')


# Задание 6
# guess_me = 7
# if guess_me < 7:
#     print('too low')
# elif guess_me > 7:
#     print('too high')
# else:
#     print('just right')


# while True:
#     guess_me = int(input('Введите число: '))
#
#     if guess_me < 8:
#         print('too low')
#     elif guess_me > 8:
#         print('too high')
#     else:
#         print('just right')
#         break


# Задание 7
# guess_me = 7
# start = 1
# while True:
#     if start < guess_me:
#         print('too low')
#     elif start == guess_me:
#         print('found it!')
#         break
#     else:
#         print('oops')
#         break
#     start += 1


# import time
# import random
# # число попыток угадать
# guesses_made = 0
# # получаем имя пользователя из консольного ввода
# name = input('Привет! Как тебя зовут?\n')
# start = time.time()
# # получаем случайное число в диапазоне от 1 до 500
# number = random.randint(1, 500)
# print(f'Отлично, {0}, я загадал число между 1 и 500. Сможешь угадать?'.format(name))
# # пока пользователь не превысил число разрешенных попыток - 6
# while guesses_made < 5:
#     # получаем число от пользователя
#     guess = int(input('Введи число: '))
#     # увеличиваем счетчик числа попыток
#     guesses_made += 1
#     if guess < number:
#         print('Твое число меньше того, что я загадал.')
#     if guess > number:
#         print('Твое число больше загаданного мной.')
#     if guess == number:
#         break
# if guess == number:
#     print(f'Ух ты, {0}! Ты угадал мое число, использовав {1} попыток!'.format(name, guesses_made))
# else:
#     print(f'А вот и не угадал! Я загадал число {0}'.format(number))
# end = time.time()
# print(f'{name} потратил - {end - start} секунд')


# Задание 8
d = {"dog": "chien", "cat": "chat", 'walrus': 'morse'}
type(d)
dict

d["walrus"]

'morse'





