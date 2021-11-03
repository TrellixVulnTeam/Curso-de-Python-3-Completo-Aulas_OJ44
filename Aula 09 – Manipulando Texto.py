"""Fatiamento de string"""

# --------------------------------------------------------------------------

print('\n   \033[1;94m+++++++\033[m \033[1;97mFatiamento\033[m \033[1;94m+++++++\033[m')

phrase = '    Curso em Vídeo Python    '

divided = phrase.split()

print(f'{divided[0][1]}\n'
      f'{phrase.count("o", 0, 14)}\n'
      f'{phrase.find("Vídeo")}\n'
      f'{phrase.lower()}\n'
      f'{phrase.split()}\n'
      f'{phrase.upper()}\n'
      f'{phrase.lower()}\n'
      f'{phrase.upper()}\n'
      f'{phrase.capitalize()}\n'
      f'{phrase.title()}\n'
      f'{phrase[:15]}\n'
      f'{phrase[::2]}\n'
      f'{len(phrase)}\n'
      f'{len(phrase.strip())}\n'
      f'{phrase.replace("Python", "Jesuss")}\n')

# --------------------------------------------------------------------------


frase = ' Curso em Vídeo Python! '
dividido = frase.split()
print(dividido[0][1])
print(frase.count('o', 0, 14))
print(frase.find('Vídeo'))
print(frase.lower())
print(frase.split())
print(frase.upper())
print(frase.capitalize())
print(frase.title())
print(frase[:15])
print(frase[::2])
print(len(frase))
print(len(frase.strip()))  # remove espaços antes e depois #
print(frase.replace('Python', 'JESU$$$'))

# --------------------------------------------------------------------------


frase = 'Curso em Video Python'
print(frase[1:15:2])
print(frase.count('o'))
print(frase.upper())
print(frase.upper().count('O'))
frase = '   Curso em Vídeo Python   !'
frase_1 = '   Aprenda Python   !'
dividido = frase.split()
frase = frase.replace('Python   !', 'JESUSSSSSSS♥').strip()
print(frase[16])
print(frase[:5])
print(frase.count('o'))  # count() pede para o programa contar por ex quantas letras "o" existem na frase
print(frase.count('O'))  # count() pede para o programa contar por ex quantas letras "o" existem na frase
print(frase.upper().count('O'))  # upper() deixa tudo maiusculo
print(len(frase.strip()))  # len() mostra o comprimento da frase em microespaços guardados na memoria
print(frase.replace('Python', 'Android'))
print(frase.find('Vídeo'))  # find() informa em que a posição que a string começou
print(frase.lower().find('vídeo'))  # lower() transforma toda a string em minuscula
print(frase.find('deo'))  # find() informa se existe a string digitada dentro da string
print(frase.replace('Python', 'iOS'))  # replace() troca uma string por outra, ex: 'python, ios'
print(frase.capitalize())  # joga a primeira letra de Cada String Para Maiúsculo
print(frase.title())  # semelhante a ao comenado .capitalize
print(frase.strip())  # Remove os espaços antes e depois da string, mas não o que separa uma palavra da outra.
print(frase_1.rstrip())  # remove os espaços da direita
print(frase.lstrip())  # remove os espaços da esquerda.
print(frase.split())
print(dividido[0])
print(dividido[2][3])
print(frase_1)
print('Curso' in frase)
print('Curso' in frase_1)
print('-'.join(frase_1), '\n\n Fim do exercício!')

# --------------------------------------------------------------------------
