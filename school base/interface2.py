from interface1 import menu_teacher,menu_student


def init():
    while True:
        print('1. Преподователь.\n2. Ученик.\n3. Выход.')
        who_ =input('Кто вы?\n  Выберите пункт меню: ')
        if who_ == '1':
            print(menu_teacher())
        elif who_ == '2':
            print(menu_student())
        elif who_ == '3':
            break
        else:
            print('Неправильный ввод!\n Выберите ещё раз. ')