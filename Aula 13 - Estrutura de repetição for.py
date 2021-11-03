# ALT+205 ═
# ALT+201 ╔
# ALT+187 ╗
# ALT+188 ╝
#  alt + 219 █
# alt + 220 ▄
# ALT+200 ╚
# --------------------------------------------------------------------------

print('\033[1;94m-=-\033[m' * 18,
      '\n\033[97m              Estruturas de repetição for'
      )
print('\033[1;94m-=-\033[m' * 18, '\n\033[97m')

inicio = int(input('  Início:...'))
fim = int(input('  Fim:......'))
passo = int(input('  Passo:....'))

for c in range(inicio, fim + 1, passo):
    print('\033[1;91m →', c, end='\033[m\033[97m')
print('\n  Seu cógido acaba bem aqui!')

# --------------------------------------------------------------------------


# i = int(input('Inicio: '))
# f = int(input('fim: '))
# p = int(input('passo: '))
# for variavel_controle in range(i, f+1, p):
#     print(variavel_controle)
# print('\n  Seu código acaba aqui.')

# --------------------------------------------------------------------------


for variavel_controle in range(0, 50, 2):  # 0 = começo, 50 = fim, 2 = passo, ou seja, de 2 em 2
    print(variavel_controle)
print('End')

for variavel_controle in range(6, 0, -1):
    print(variavel_controle)

# --------------------------------------------------------------------------


soma = 0
for variavel_controle in range(0, 3):
    nu = int(input('Digite um valor: '))
    soma += nu
print(soma, '\nSeu código acaba aqui.')

# --------------------------------------------------------------------------


s = 0
for variavel_controll in range(0, 4):
    num = int(input('Digite um valor:'))
    s += num
print(variavel_controll)

# --------------------------------------------------------------------------
