"""Nessa aula, vamos aprender o que são LISTAS e como
utilizar listas em Python. As listas são variáveis
compostas que permitem armazenar vários valores e
uma mesma estrutura, acessíveis por chaves individuais."""
# ----------------------------------------------------------------------

teste = list()
galera = list()

teste.append('Kennedy'), teste.append(28)

galera.append(teste[:])  # copiando uma lista

teste[0] = 'Maria'
teste[1] = 22

galera.append(teste[:])  # copiando uma lista

print(galera)


print('\n')
# ----------------------------------------------------------------------

Galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]

print(Galera)  # mostra a lista toda
print(Galera[0])  # ['João', 19]
print(Galera[0][0])  # João
print(Galera[2][1])  # 13

for pessoa in Galera:  # para cada pessoa em Galera
    print(f'{pessoa[0]} tem {pessoa[1]} anos de idade.')


print('\n')
# ----------------------------------------------------------------------

galera = list()  # estrutuda de dados composta
dado = list()    # estrutuda de dados composta auxiliar (temporária)

total_maior = total_menor = 0

for contador in range(0, 3):
    dado.append(str(input('Nome:....')))  # vai ler tudo em string
    dado.append(int(input('Idade:...')))  # vai ler qualquer valor numérico como inteiro
    galera.append(dado[:])  # copia da lista dado [:]
    dado.clear()  # limpa a lista a cada LOOP

for pessoa in galera:
    if pessoa[1] >= 18:
        total_maior += 1
        print(f'{pessoa[0]} é maior de idade')
    else:
        total_menor += 1
        print(f'{pessoa[0]} é menor de idade')

print(f'Temos {total_maior} maiores e {total_menor} memores de idade.')


print('\n')
# ----------------------------------------------------------------------

dados = list()
dados1 = list()
dados2 = list()

dados.append('Pedro'), dados.append(25)
dados1.append('Maria'), dados1.append(19)
dados2.append('João'), dados2.append(32)

print(dados[0])  # Pedro
print(dados[1])  # 25

Pessoas = list()

Pessoas.append(dados)   # copiando uma estrutura composta para dentro de outra
Pessoas.append(dados1)  # copiando uma estrutura composta para dentro de outra
Pessoas.append(dados2)  # copiando uma estrutura composta para dentro de outra

print(Pessoas)
print(Pessoas[0][0])  # Pedro
print(Pessoas[1][1])  # 19
print(Pessoas[2][0])  # João
print(Pessoas[1])  # ['Maria', 19]


print('\n')
# ----------------------------------------------------------------------

dados = list()

dados.append('Pedro'), dados.append('Thiago'), dados.append('e')
dados.append('João'), dados.append('no'), dados.append('barquinho')

print(dados[0], end=', ')  # Pedro
print(dados[1], end=' ')   # Thiago
print(dados[2], end=' ')
print(dados[3], end=' ')
print(dados[4], end=' ')
print(dados[5], end=' ')


print('\n')
# ----------------------------------------------------------------------
# fatiamento completo de uma estrutura de dados, ou seja,
# copia uma lista completa para dentro de outra lista

pessoas = list()

pessoas.append(dados)

print(pessoas)

pessoas = [['Pedro'], ['Thiago'], ['e'], ['João'], ['no'], ['barquinho']]

print(f'{pessoas[0][0]}, '  # Pedro
      f'{pessoas[1][0]} '   # Thiago
      f'{pessoas[2][0]} '   # e
      f'{pessoas[3][0]} '   # João
      f'{pessoas[4][0]} '   # no
      f'{pessoas[5][0]} '   # barquinho
      )

# ----------------------------------------------------------------------
