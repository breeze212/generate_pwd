from random import *


digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
count_pwd = int(input('Введите количество создаваемых паролей: '))
count = 0
chars = ''

dig_on = input('Включать ли цифры 0123456789? (y/n) ').lower()
if dig_on in ['да', 'д', 'l', 'lf', 'y', 'yes']:
    chars += digits
abc_upper = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (y/n) ')
if abc_upper in ['да', 'д', 'l', 'lf', 'y', 'yes']:
    chars += lowercase_letters
abc_lower = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (y/n) ')
if abc_lower in ['да', 'д', 'l', 'lf', 'y', 'yes']:
    chars += uppercase_letters
ch_on = input('Включать ли символы !#$%&*+-=?@^_? (y/n) ')
if ch_on in ['да', 'д', 'l', 'lf', 'y', 'yes']:
    chars += punctuation
exc_on = input('Исключать ли неоднозначные символы il1Lo0O? (y/n) ')
if exc_on in ['да', 'д', 'l', 'lf', 'y', 'yes']:
    for i in ('il1Lo0O'):
        if i in chars:
            chars = chars.replace(i, '')

def generate_pwd():
    pwd = ''
    len_pwd = int(input('Укажите длину пароля: '))
    for i in range(len_pwd):
        pwd += choice(chars)
    return pwd


def create_pwd_count():
    for i in range(count_pwd):
        print(generate_pwd())


create_pwd_count()
