# Домашнее задание по теме "Try и Except"

# Задание "Программистам всё можно":

def add_everything_up(a, b):
    try:
        s = a + b
        return round(s, 3)
    except TypeError:
        return f'{a}{b}'
print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))


