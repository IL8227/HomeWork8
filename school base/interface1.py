from write_read import *



def write_items():
    print('1. История\n2. География\n3. Литература\n4. Выход')
    n = input('Выберите ваш предмет. ')
    while True:
        if n == '1':
            hw_history()
            break
        elif n == '2':
            hw_geography()
            break
        elif n == '3':
            hw_literature()
            break
        elif n == '4':
            break
        else:
            print('Неправильный ввод!\n Выберите ещё раз. ')

def read_items():
    print('1. История\n2. География\n3. Литература\n4. Выход')
    n = input('Выберите ваш предмет. ')
    while True:
        if n == '1':
            read_hw_h()
        elif n == '2':
            read_hw_g()
        elif n == '3':
            read_hw_l()
        elif n == '4':
            break
        else:
            print('Неправильный ввод!\n Выберите ещё раз. ')


def menu_student():
    print(' 1. История\n 2. География\n 3. Литературв\n 4. Список преподователей\n 5. Выход')
    menu_item = input('Выберите пункт меню ')
    while True:
        if menu_item == '1':
            read_hw_h()
            break
        elif menu_item == '2':
            read_hw_g()
            break
        elif menu_item == '3':
            read_hw_l()
            break
        elif menu_item == '4':
            read_teach()
            break
        elif menu_item == '5':
            break
        else:
            print('Неправильный ввод!\n Выберите ещё раз.')


def menu_teacher():
    print(' 1. Текущее домашнее задание.\n 2. Задать новое задание.\n 3. Список учеников.\n '
              '4. Добавить нового ученика.\n 5. Выход')
    menu_item = input('Выберите пункт меню. ')
    while True:
        if menu_item == '1':
            read_items()
            break
        elif menu_item == '2':
            write_items()
            break
        elif menu_item == '3':
            read_names()
            break
        elif menu_item == '4':
            write_name()
            break
        elif menu_item == '5':
            break
        else:
            print('Неправильный ввод!\n Выберите ещё раз.')