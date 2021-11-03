num = [2, 5, 9, 1]
num[2] = 3
num.append(7)  # adicionando o valor 7 ao ultimo elemento
num.sort()  # ordem
num.sort(reverse=True)  # ordem inversa
num.insert(2, 2)  # na posição 2 insira o valor 2
num.remove(
    2)  # procura do inicio da lista a primeira ocorrencia do valor que vc deseja eliminar, e elimina, ele n varre até o final
num.pop()  # elimina o último valor da lista se não houver nenhum parametro
if 4 in num:
    num.remove(4)
else:
    print('O elemento 4 não foi encontrado na lista.')

print(num)
print(f'Esta lista contém {len(num)} elementos.\n\n')  # mostra o comprimento da lista

# --------------------------------------------------------------------------

valoress = list()

valoress.append(5)
valoress.append(9)
valoress.append(4)

for v in valoress:
    print(f'{v}...', end='')

# --------------------------------------------------------------------------

valoress = list()

valoress.append(5)
valoress.append(9)
valoress.append(4)

for chave, valores in enumerate(valoress):
    print(f'Na posição {chave} encontrei o valor {valores}')
print('Fim da lista.')

# --------------------------------------------------------------------------

a_lista = [2, 3, 4, 7]
b_lista = a_lista  # aqui se faz uma ligação entre as listas, logo se alterar o elemento da b_lista também será alterado na a_lista.
be_lista = a_lista[:]  # aqui é feita uma copia da lista, podendo ser alterado o item da lista sem mudar o da outra
b_lista[2] = 8  # aqui é alterado na posição 2 o elemento para o valor 8 em ambas as listas

print(f'Lista A: {a_lista} \n'
      f'Lista B: {b_lista}')

# --------------------------------------------------------------------------

valoress = list()

for contador in range(0, 5):
    valoress.append(int(input('Digite um valor para ser adicionado ao final da lista: ')))

for chave, valor in enumerate(valoress):
    print(f'Encontrei o valor {valor} na posição {chave} \n')

print(f'{valoress}'
      f'Fim da lista')
# --------------------------------------------------------------------------

lista_lanches = ['Hamburguer', 'Suco', 'Pizza', 'Pudim de Leite']

print(f' {lista_lanches[2]}')  # imprime a pizza, ou seja, o elemento 2

print(lista_lanches[3])

# --------------------------------------------------------------------------

lista_lanches[3] = 'Picole'  # substitui o elemento 3 da lista, ou seja, o Pudim de Leite
print(lista_lanches)

# --------------------------------------------------------------------------

lista_lanches.append('Cookies')  # .append adiciona um elemento no final da lista

# --------------------------------------------------------------------------

lista_lanches.insert(0, 'Cachorro-quente')  # adiciona um elemento a lista na posição desejada.
print(lista_lanches)

# --------------------------------------------------------------------------
# se voce quiser eliminar um elemento da lista pelo seu índice,
# use .pop() ou del
# se voce deseja eliminar pelo conteúdo, ou seja, pelo valor use o .remove()
del lista_lanches[3]  # apaga o elemento 3 da lista
print(lista_lanches)

lista_lanches.pop()  # pop normalmente é para eliminar o ultimo elemento,
print(lista_lanches)  # porem voce pode passar o parametro desejado para que seja eliminado

lista_lanches.remove('Suco')  # remove elimina um elemento da lista pelo seu valor e não pelo índice
print(lista_lanches)

# --------------------------------------------------------------------------

if 'Pizza' in lista_lanches:  # se existir Pizza em lista_lanches
    lista_lanches.remove('Pizza')  # remova  a Pizza

# --------------------------------------------------------------------------

valores = list(range(4, 11))  # criando uma estrutura composta
print(valores)  # ordenada nesse caso do 4 ao 10, pq o 11 é ignorado

# --------------------------------------------------------------------------

values = [8, 2, 5, 4, 9, 3, 0]

values.sort()  # ordena os valores em ordem crescente, ou alfabética
print(values)

values.sort(reverse=True)  # ordena de maneira inversa, ou seja, descrecente no caso de valores numéricos
print(values)

print(len(valores))  # mostra o comprimento da lista

# --------------------------------------------------------------------------
