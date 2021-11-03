pessoas = {'nome':'Gustavo', 'sexo': 'M', 'idade': 22}

pessoas['peso'] = 96.58

print(f'{pessoas["nome"]} tem {pessoas["idade"]} anos')
print(pessoas.keys())  # mostra as chaves do dicionario: "nome", "sexo" e "idade"
print(pessoas.values())  # mostra os valores do dicionário: 'gustavo', 'M' e '22'
print(pessoas.items())

for k, v in pessoas.items():
    print(f'{k}: {v}')

print()
# ----------------------------------------------------------------------------------

brasil = []

estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}

brasil.append(estado1), brasil.append(estado2)

print(brasil[0])  # corresponde ao primeiro item que foi adicionado, ou seja, o primeiro dicionário
print(brasil[0]['uf'])  # corresponde ao estado do RIO DE JANEIRO
print(brasil[1]['sigla'])  # corresponde a SIGLA de SÃO PAULO

print()
# ----------------------------------------------------------------------------------

estado = dict()
brasil = list()

for cont in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa:'))
    estado['sigla'] = str(input('Sigla do estado: '))

    brasil.append(estado.copy())  # copy() é usado para copiar um dicionario

for est in brasil:
    for k, v in est.items():
        print(f' O campo {k} tem valor {v}')
