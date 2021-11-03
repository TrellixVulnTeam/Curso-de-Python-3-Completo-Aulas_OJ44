
aula07 = '---- Aula 07 ----'
aula = 'Operadores Aritméticos!'

print(f'{aula07:^22}\n\n{aula}\n')

# --------------------------------------------------------------------------

print(5 + 3 * 2)  # Resultado: 11
print(3 * 5 + 4 ** 2)  # Rsultado:  31
print(3 * (5 + 4) ** 2)  # Resultado: 243

# --------------------------------------------------------------------------

name = input('Informe o seu nome: ')

print(f'É um prazer te conhecer {name}')
print(f'É um prazer te conhecer {name:#^20}')
print(f'É um prazer te conhecer {name:=>20}')
print(f'É um prazer te conhecer {name:=<20}')
print(f'É um prazer te conhecer {name:=^20}\n')

# --------------------------------------------------------------------------

print(f'É um prazer te conhecer {name}', end=' ')
print(f'É muito bom te conhecer, jovem {name:#>20}', end=' ')  # o comando " end='' " indica que a linha não acabou
print(f'É muito bom te conhecer, jovem {name:=>20}', end=' ')
print(f'É muito bom te conhecer, jovem {name:!<20}', end=' ')
print(f'É muito bom te conhecer, jovem {name:>20}', end=' ')
print(f'É muito bom te conhecer, jovem {name:=^20}\n')

# --------------------------------------------------------------------------

print(f'\n É muito bom te ver, {name}!\n É muito bom te ver {name:#>20}!\n É muito bom te ver {name:~<20}!\n É muito bom te ver {name:@^20}!\n É muito bom te ver {name:*>20}!\n É muito bom te ver {name:*<20}!')

# --------------------------------------------------------------------------

number1 = int(input('Informe um valor: '))
number2 = int(input('Informe outro valor: '))

soma = number1 + number2
multiplication = number1 * number2  # multiplicação
division = float(number1 / number2)  # divisão inteira
whole_division = number1 // number2  # resto da divisão
exponentiation = number1 ** number2  # exponenciação

print(f'''A soma é: {soma}
- O produto é: {multiplication}
- A divisão é: {division} 
- Divisão inteira: {whole_division:.1f}
- Exponenciação: {exponentiation}''')
'''se o resultado for menor que 1.0 sempre vai retonar 0.0,
pois a divisão inteira só mostra se o resultado for inteiro
'''

# --------------------------------------------------------------------------

