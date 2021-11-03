from Uteis import numeros


# Programa Principal
numero = int(input('+------------+------------+ \n'
                   '|  Digite um valor: '))

fat = numeros.fatorial(numero)

print(f'|  O dobro de {numero} é {numeros.dobro(numero)}')
print(f'|  O triplo de {numero} é {numeros.triplo(numero)}')
print(f'|  O fatorial de {numero} é {fat} \n'
      f'+------------+------------+')
