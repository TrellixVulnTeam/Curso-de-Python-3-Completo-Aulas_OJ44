

def contador(inicio, fim, passo):
    """ \033[97m»» Faz uma contagem e mostra na tela.
            :param inicio: início da contagem
            :param fim: fim da contagem
            :param passo: passo da contagem, 2 em 2, 3 em 3, etc
            :return: sem retorno
            Função criada por Gustavo Guanabara do canal CursoemVídeo\033[m
        """

    cont = inicio
    while cont <= fim:
        print(f'{cont} ',end='')
        cont += passo
    print('\nFim!')


contador(0, 100, 5)
help(contador)

# ------------------------------------------------------------------------------
# Parâmentros opcionais


def somar(a=0, b=0, c=0):  # Parâmentro opcional
    soma = a + b + c
    print(f'A soma entre {a}, {b} e {c} é igual a {soma}')


somar(3, 2, 5), somar(8, 4)
somar(), somar(b=4, c=2)
somar(c=3, a=2), somar(a=100, b=500, c=400)

# ------------------------------------------------------------------------------
# Escopo de Variáveis


def teste():
    x = 8  # Variável LOCAL
    print(f'Na função teste, num vale {num}')
    print(f'Na função teste, X vale {x}')


# Programa Principal
num = 2  # variável GLOBAL

print(f'No programa principal, num vale {num}')

teste()
# ------------------------------------------------------------------------------


def test(b):
    global a  # usando este comando GLOBAL a váriavel |a| não será mudada fora do escopo
    a = 8
    b += 4
    c = 2
    print(f'A dentro do escopo vale {a}')
    print(f'B dentro do escopo vale {b}')
    print(f'C dentro do escopo vale {c}')


# Programa Principal
a = 5

test(a)

print(f'A fora do escopo vale {a}')

# ------------------------------------------------------------------------------


def funcao():
    n1 = 4
    print(f'N1 dentro do escopo (VARIÁVEL LOCAL) vale {n1}')


n1 = 2

funcao()

print(f'N1 fora do escopo (VARIÁVEL GLOBAL) vale {n1}')

# ------------------------------------------------------------------------------
# Retornando Valores


def somar(a=0, b=0, c=0):
    soma = a + b + c
    return soma


# Programa Principal
r1 = somar(3, 2, 5)
r2 = somar(2, 2)
r3 = somar(6)

print(f'Os resultados das somas foram {r1}, {r2} e {r3} respectivamente')

# ------------------------------------------------------------------------------


def fatorial(nu=1):
    fat = 1
    for cont in range(nu, 0, -1):
        fat *= cont
    return fat


f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()

print(f'Os resultados são {f1}, {f2} e {f3}')

n = int(input('\nDigite um número para retornar o seu fatorial: '))

print(f'O factorial de {n} é igual a {fatorial(n)}')

# ------------------------------------------------------------------------------


def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número: '))

if par(num):
    print('É par!')
else:
    print('É ímpar!')

# ------------------------------------------------------------------------------

