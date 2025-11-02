import argparse
import string
import secrets
import sys

# Константы по умолчанию, если пользователь не укажет параметры --length или --number
DEFAULT_LENGTH = 12
DEFAULT_COUNT = 5

# Эта функция собирает «набор символов» — алфавит, из которого будут случайно выбираться символы для пароля.
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
def generate_password(length, charset):
    if length <= 0:
        raise ValueError("Длина должна быть положительной")
    if not charset:
        raise ValueError('Charset пуст!')
    return ''.join(secrets.choice(charset) for _ in range(length))

#Создаёт CLI-интерфейс
def parse_args():
    p = argparse.ArgumentParser(description='Генератор паролей')
    p.add_argument('-l', '--length', type=int, default=12, help='длина пароля')
    p.add_argument('-n', '--number', type=int, default=5, help='количество паролей')
    p.add_argument('--no-letters', dest='letters', action='store_false',help='не включать буквы')
    p.add_argument('--no-digits', dest='digits', action='store_false',help='не включать цифры')
    p.add_argument('--specials', dest='specials', action='store_true',  help='включить спецсимволы')
    p.set_defaults(letters = True, digits = True, specials = False)
    return p.parse_args()

def main():
    args = parse_args()
    try:
        charset = make_charset(args.letters, args.digits, args.specials)
        for i in range(1, args.number + 1):
            print(f'{i:2d}: {generate_password(args.length, charset)}')
    except ValueError as e:
        print('Ошибка:', e, file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()