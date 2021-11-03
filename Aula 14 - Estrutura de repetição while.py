from time import sleep

# c = 1  # aqui o c é o 1 que é o inicio do RANGE
# while c in range(0, 10):
#     sleep(0.5)
#     c += 1
#     print(c)
# for c in range(1, 3):
#     sleep(0.3)
#     print(c)

# c = 1
# while c < 10: # enquanto o contador for menor que 10
#     print(c)
#     sleep(0.3)
#     c = c + 1
# print('End.')

# r = 'S'
# while r == 'S':
#     n = int(input('Informe um valor :'))
#     r = str(input('Deseja continuar? [S/N] ')).upper()
# print('FIM')
#
# n = 1
# while n != 0:  # Enquanto o valor for DIFERENTE !=  de 0, continue o laço
#     n = int(input('Valor :'))
# print('Fim')

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 ==0:
            par += 1
        else:
            impar += 1
print(f'vc digitou {par} numeros pares  e {impar } numeros impares')
