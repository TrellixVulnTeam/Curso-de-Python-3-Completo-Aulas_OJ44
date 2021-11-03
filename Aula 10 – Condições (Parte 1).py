"""Nessa aula, vamos aprender como utilizar estruturas condicionais
simples e compostas nos seus programas em Python."""

# --------------------------------------------------------------------------

print('     #====== Estruturas Condicionais simples ======#\n')

# --------------------------------------------------------------------------

num1 = float(input('        Primeira nota: '))
num2 = float(input('        Segunda nota:'))

media = (num1 + num2) / 2

print(f'        A média do aluno é: {media}')

if media >= 6:
    print('\n        Approved!')
else:
    print('\n        Disapproved!')

# --------------------------------------------------------------------------


nome = str(input('Qual é o seu nome? ')).strip()
if nome == 'Davyd Kennedy':
    print('Nome legal')
else:
    print('Seu nome é tão normal! kk')

# --------------------------------------------------------------------------


n1 = float(input('\033[1mDigite a primeira nota: \033[m'))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print(f'A sua \033[1;4mmédia\033[m foi: \033[1;32m{m:.1f}\033[m')
if m >= 6.0:
    print(f'Voce foi aprovado!')
else:
    print('\033[31mkkkkk.. não foi dessa vez.\033[m')


nome = int(input('Em qual ano seu Bel nasceu?? '))
if nome <= 2016:
    print('\nEntão seu filho vai completar 5 anos?')
else:
    n1 = str(input('Então seu filho tem 4 anos?'))

# --------------------------------------------------------------------------

age = int(input('           Há quanto tempo você é casado? '))

if age >= 7:
    print('           Bastante tempo hein guerreiro!')
else:
    print(f'           Só {age} ano(s)?!\n'
          f'           Será que aguenta muito tempo ainda? kkk')

# --------------------------------------------------------------------------

tempo = int(input('Quantos anos tem seu carro?'))
if tempo <= 3:
    print('Carro novo!')
else:
    print('Carro velho\n --FIM--')

# --------------------------------------------------------------------------

tempo = int(input('Quantos anos tem seu carro?'))

# condição simplificada pode ser usada em uma linha só em algumas situaçoes mais "simples"
print('Carro do ano KKK' if tempo <= 4 else 'Sucata... kkkkk\n\n --- Fim ---\n\n\n')