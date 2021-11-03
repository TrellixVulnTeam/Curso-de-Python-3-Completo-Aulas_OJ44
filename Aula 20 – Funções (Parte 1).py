

# def ponto():
#     print('·' * 30)
#
#
# # Programa Principal
# ponto()
# print(' Curso em Vídeo ')
# ponto()
# print(' Aprenda Python ')
# ponto()
# print(' Gustavo Guanabara ')
# ponto()


# ======================================================================================================


def mensagem(msg):
    print('\033[91m○\033[m' * 20)
    print(msg)
    print('\033[91m○\033[m' * 20)


mensagem('  Sitema de alunos')

# ======================================================================================================


def titulo(txt):
    print('\033[91m○\033[m' * 30)
    print(txt)
    print('\033[91m○\033[m' * 30)


# Programa Principal
titulo('      CURSO EM VÍDEO  ')
titulo('      APRENDA PTYHON  ')
titulo('      GUSTAVO GUANABARA  ')
titulo('      PYTHON É MUITO BOM  ')

# =======================================================================================================


def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A + B = {s}\n')


# Programa Principal
soma(4, 5), soma(8, 9), soma(2, 1)
soma(111, 2), soma(555, 111), soma(7, 2)

soma(b=4, a=5)  # inverter de a+b para b+a

# =======================================================================================================


def contador(* num):
    for valor in num:
        print(f'{valor} ', end='')
    print('Fim')


# Programa Principal
contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

# =======================================================================================================


def contador(*num):
    tamanho = len(num)
    print(f'Recebi os valores {num} que são ao todo {tamanho} números')


# Programa Principal
contador(2, 1)
contador(2, 5, 8, )
contador(1, 5, 9, 6, 3)
contador(5, 666)

# =======================================================================================================


def dobrar(lst):
    position = 0
    while position < len(lst):
        lst[position] *= 2
        position += 1


lista_de_valores = [7, 2, 5, 0, 4]
dobrar(lista_de_valores)
print(lista_de_valores)

# =======================================================================================================


def somar(* valores):
    som = 0
    for numero in valores:
        som += numero
    print(f'Somando os valores {valores} temos {som}')


# Programa Principal
somar(5, 2)
somar(2, 9, 4)

# =======================================================================================================
