lanche = 'Burguer', 'suco', 'pizza', 'pudim'  # TUPLAS.

print(f'{lanche} \n'
      f'{lanche[0:2]} \n'
      f'{len(lanche)}')  # durante o fatiamento, o último elemento é é ignorado.

# --------------------------------------------------------------------------

lanche = 'Burguer', 'suco', 'pizza', 'pudim'  # TUPLAS.

for c in lanche:  # para cada c in lanche
    print(c)

# --------------------------------------------------------------------------

lanche = 'Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata frita'

print(
    f'{lanche} \n'
    f'{lanche[1]} \n'
    f'{lanche[-2]} \n'
    f'{lanche[-3]} \n'
    f'{lanche[1].upper()} \n'
    f'{lanche[2].lower()} \n'
    f'{lanche[1:3]} \n'  # fatiamento sempre desconsidera o ÚLTIMO elemento da tupla
    f'{lanche[3:]} \n'
    f'{len(lanche)}, o len() retorna o comprimento da lista, tupla ou o que for. '
)

# --------------------------------------------------------------------------

for rango in lanche:
    print(f'Eu vou comer {rango}')
print('Comi p porra')

# --------------------------------------------------------------------------

for cont in range(0, len(lanche)):
    print(f'eu ja comi {lanche[cont]}')
print('To cheio KKK')

# --------------------------------------------------------------------------

for pos, comida in enumerate(lanche):  # enumerate retorna tanto o dado quanto a posição
    print(f'Eu to comendo {comida} na posição {pos}')

# --------------------------------------------------------------------------

lanche = 'Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batara frita'

print(sorted(lanche))  # mostra a tupla em ordem

# --------------------------------------------------------------------------

tupla_a = 2, 5, 4
tupla_b = 5, 8, 1, 2
c = tupla_a + tupla_b

print(c)
print(len(c))  # retorna o comprimento
print(c.count(5))  # ou seja quantas vezes aparece o numeral 5 na variavel c
print(c.index(8))  # retorna  a posição do elemento na lista/tupla/dicionário
print(c.index(4))  # retorna  a posição do elemento na lista/tupla/dicionário
print(c.index(5, 1))  # descolamento para contar a posição do elemento a partir da posição 1 e não 0 como é por padrão.

# --------------------------------------------------------------------------

pessoa = 'nome', 'kennedy', 'idade', 28, 'Sexo', 'Masculino', 'Peso', '96.50',
# del pessoa  # deleta uma tupla inteira.
print(pessoa)
