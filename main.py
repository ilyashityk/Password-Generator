from random import randint


def int_foolproof(number):
    while True:
        if number.isdigit() and number != '0':
            return number
            break
        else:
            print('Please enter a valid number.')
            number = input()


def str_foolproof(string):
    while True:
        if string == 'y' or string == 'n':
            return string
            break
        else:
            print('Please enter a valid answer (y/n)')
            string = input()


def chars_enter():
    global p_digits_on, p_ABC_on, p_abc_on, p_symbols_on, p_strange_off
    while True:
        p_digits_on = input('Include digits "0123456789"? (y/n)')
        p_digits_on = str_foolproof(p_digits_on)
        p_ABC_on = input('Include uppercase letters "ABCDEFGHIJKLMNOPQRSTUVWXYZ"? (y/n)')
        p_ABC_on = str_foolproof(p_ABC_on)
        p_abc_on = input('Include lowercase letters "abcdefghijklmnopqrstuvwxyz"? (y/n)')
        p_abc_on = str_foolproof(p_abc_on)
        p_symbols_on = input('Do the characters "!#$%&*+-=?@^_"? (y/n)')
        p_symbols_on = str_foolproof(p_symbols_on)
        p_strange_off = input('Do I exclude ambiguous characters "il1Lo0O"? (y/n)')
        p_strange_off = str_foolproof(p_strange_off)
        if p_digits_on == 'n' and p_ABC_on == 'n' and p_abc_on == 'n' and p_symbols_on == 'n':
            print("Bro, password can't be empty. Let's start again :(")
        else:
            break


def chars_generator():
    global chars
    if p_digits_on == 'y':
        chars += DIGITS
    if p_ABC_on == 'y':
        chars += UPPERCASE_LETTERS
    if p_abc_on == 'y':
        chars += LOWERCASE_LETTERS
    if p_symbols_on == 'y':
        chars += PUNCTUATION
    if p_strange_off == 'y':
        for c in 'il1Lo0O':
            chars = chars.replace(c, '')


def generate_password(length, chars):
    for _ in range(int(p_count)):
        print(*(chars[randint(0, len(chars)-1)] for _ in range(int(length))), sep='')


DIGITS = '0123456789'
LOWERCASE_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
UPPERCASE_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
PUNCTUATION = '!#$%&*+-=?@^_'
chars = ''

print('Welcome to Password Generator, my friend! Now i will ask you a few questions.')

p_count = input('Specify the quantity of passwords to generate:')
p_count = int_foolproof(p_count)
p_length = input('Specify the length of one password:')
p_length = int_foolproof(p_length)

chars_enter()
chars_generator()
generate_password(p_length, chars)
