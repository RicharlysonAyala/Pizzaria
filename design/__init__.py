def line(tam=42):
    return '\033[1;30m-'* tam


def header(txt):
    print(line())
    print(txt.center(42))
    print(line())


def menu(lista):
    header('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[1;33m{c}\033[1;30m - \033[1;34m{item}\033[m')
        c += 1
    print(line())