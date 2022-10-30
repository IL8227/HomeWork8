def write_name():
    surname = input('Введите фамиилию нового ученика. ')
    name = input('Введите имя нового ученика. ')
    with open('names.txt','a',encoding='utf-8') as n:
        n.write(f'{surname};{name}\n')

def hw_history():
    h_w = input('Введите домашнее задание.')
    with open('hw_history.txt','a',encoding='utf-8') as f:
        f.write(f'{h_w}\n')

def hw_geography():
    h_w = input('Введите домашнее задание.')
    with open('hw_geography.txt','a',encoding='utf-8') as f:
        f.write(f'{h_w}\n')

def hw_literature():
    h_w = input('Введите домашнее задание.')
    with open('hw_literature.txt','a',encoding='utf-8') as f:
        f.write(f'{h_w}\n')

def read_hw_h():
    with open('hw_history.txt','r',encoding='utf-8') as g:
        hw = g.read()
        print(hw)

def read_hw_g():
    with open('hw_geography.txt','r',encoding='utf-8') as g:
        hw = g.read()
        print(hw)

def read_hw_l():
    with open('hw_literature.txt','r',encoding='utf-8') as g:
        hw = g.read()
        print(hw)
def read_names():
    with open('names.txt','r',encoding='utf-8') as n:
        names = n.read()
        print(names)

def read_teach():
    with open('teachers.txt','r',encoding='utf-8') as t:
        teacher = t.read()
        print(teacher)