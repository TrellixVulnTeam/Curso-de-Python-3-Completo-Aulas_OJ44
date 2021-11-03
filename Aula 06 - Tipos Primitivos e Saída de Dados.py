number1 = int(input('Informe um valor: '))
print(type(number1))  # informa a classe do que foi digitado no INPUT

# --------------------------------------------------------------------------

number1 = int(input('Informe um número: '))
number2 = int(input('Informe outro número: '))
soma = number1 + number2
print(f'A soma vale: {soma}')

# --------------------------------------------------------------------------

numb1 = float(input('Informe um número: '))
numb2 = float(input('Informe outro número:'))
soma = numb1 + numb2
print(f'A soma vale: {soma:.2f}')

# --------------------------------------------------------------------------

num1 = int(input('Informe um número: '))
num2 = int(input('Informe outro número: '))
soma = num1 + num2
print(f'Somando {num1} com {num2} temos: {soma}')

# --------------------------------------------------------------------------

nu1 = int(input('Informe um número: '))
nu2 = int(input('Informe outro número: '))
multi = nu1 * nu2
print(f'{nu1} multiplicado por {nu2} é igual a: {multi}')

# --------------------------------------------------------------------------

nu = str(input('Informe um valor: '))
print(f'O número {nu} é da classe: {type(nu)}') # mostra que o número esclhido é da classe string

# --------------------------------------------------------------------------

number = float(input('Informe um valor: '))
print(f'\nO número {number} é da classe: {type(number)}') # mostra que o número esclhido é da classe float

# --------------------------------------------------------------------------

''' Em Python, uma variável pode assumir valor booleano True (verdadeiro) ou False (falso).
Esses valores são úteis para representar, por exemplo,
o resultado de uma comparação. Experimente: '''


a = 3
b = 4
c = a < b
d = a > b
e = a == b
print(f'Valor de c: {c}')
print(f'Valor de d: {d}')
print(f'Valor de e: {e}')

# --------------------------------------------------------------------------

number = bool(input('Informe um número: '))
print(f'\nO número {number} escolhido é da classe: {type(number)}')
print(type(number))

# --------------------------------------------------------------------------

a = input('Escreva qualquer coisa: ')
print(f'Só tem espaçoes? {a.isspace()}')
print(f'É numérico? {a.isnumeric()}')
print(f'É alfabético? {a.isalpha()}')
print(f'É alfanumérico? {a.isalnum()}')
print(f'Está em maiúsculas? {a.isupper()}')
print(f'Está em minúsculas? {a.islower()}')
print(f'Está capitalizada? {a.istitle()}')

# --------------------------------------------------------------------------
