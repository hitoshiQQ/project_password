import argparse
import string
import secrets
import sys

# Константы по умолчанию, если пользователь не укажет параметры --length или --number
DEFAULT_LENGTH = 12
DEFAULT_COUNT = 5

# Эта функция собирает «набор символов» — алфавит, из которого будут случайно выбираться символы для пароля.
# В зависимости от аргументов пользователь может включить или выключить разные типы символов.
# Если пользователь не выберет ничего (например, выключит и буквы, и цифры), 
# функция вернёт пустую строку — программа позже отловит это и покажет ошибку.
def make_charset(use_letters = True, use_digits = True, use_specials=False):
    chars = ''
    if use_letters:
        chars += string.ascii_letters # 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if use_digits:
        chars += string.digits        # '0123456789'
    if use_specials:
        chars += string.punctuation   # '!@#$%^&*()_+...'
    return chars

#Генерирует один пароль заданной длины.
# Проверяет, что длина положительная и набор символов не пустой.
# Затем с помощью secrets.choice() выбирает каждый символ случайно из charset.
# secrets.choice() безопасен — он не предсказуем, в отличие от random.choice().
# Результат — строка, состоящая из length случайных символов.
def generate_password(length, charset):
    if length <= 0:
        raise ValueError("Длина должна быть положительной")
    if not charset:
        raise ValueError('Charset пуст!')
    return ''.join(secrets.choice(charset) for _ in range(length))

