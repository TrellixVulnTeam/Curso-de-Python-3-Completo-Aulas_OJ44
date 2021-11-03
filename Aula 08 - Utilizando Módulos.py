import math
import emoji
import random

lesson = ':alien: Aula 08 :alien:'
print(emoji.emojize(f'{lesson:^40} \n', use_aliases=True))

number = int(input('Informe um número: '))
root = math.sqrt(number)
print(f'\nA Raiz Quarada exata de: {number} é: {root:.2f}')  # raiz exata.
print(f'A Raiz Quadrada de: {number} arredondada para cima é: {math.ceil(root):.2f}')  # .ceil vai arredondar para cima.
print(f'A Raiz Quadrada de: {number} arredondada para baixo é: {math.floor(root):.2f}')  # .floor arredonda para baixo.

num = int(input('Informe um número: '))
square_root = math.sqrt(num)
print(f'A Raiz Quadrada exata de: {num} é : {square_root:.2f}')  # Raiz Quadrada exata.
print(f'A Raiz Quadrada de: {num} arredondada para cima é: {math.ceil(square_root):.2f}')  # Raiz² arredondada para cima.
print(f'A Raiz Quadrada de: {num} arredondada para cima é: {math.floor(square_root):.2f}')  # Raiz² arredondada para baixo.

number0 = random.randint(0, 100)  # Randomiando um número; nesse caso entre 0 e 100.
print(f'Seu número Random é: {number0}')

from math import sqrt  # para consumir menos memoria, se precisar apenas uma função de determiado módulo escreva ' from import '
number_1 = int(input('Informe um número: '))
raizq = sqrt(number_1)
print(f'\nA Raiz exata de {number_1} é: {raizq:.2f}')

print(emoji.emojize('Hello, World! :earth_americas:', use_aliases=True))
print(emoji.emojize('Python é vida! :thumbs_up:', use_aliases=True))
print(emoji.emojize('Python é Amor kkkk :red_heart:', use_aliases=True))
print(emoji.emojize('Python é :red_heart:', variant='emoji_type'))
print(emoji.emojize('Python é :red_heart:', variant='emoji_type'))
