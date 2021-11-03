from time import sleep

# cont = 1
# while cont <= 10:
#     sleep(0.35)
#     print('\033[1;32m', cont, '-> \033[m', end='')
#     cont += 1
# print("\nEND")
# --------------------------------------------------------------------------

# # cont = 1
# while True:  # while para sempre.
#     print(cont, '-> ', end='')
#     cont += 1
# print('End')

# --------------------------------------------------------------------------

# n = cont = 0
# while cont < 3:
#     n = int(input('Número: '))
#     cont += 1
#
#
# num = 0
# while num != 999:
#     num = int(input('Número: '))

# --------------------------------------------------------------------------

# n = s = 0
# while n != 999:
#     n = int(input('Número: '))
#     s += n
# s -= 999  # modo gambiarra de interromper um  laço de repetição infinito while True
# print(f'A soma vale: {s}')

# --------------------------------------------------------------------------

n = s = 0  # aqui começamos as variaveis atrinbuindo o valor de 0 primeiramente.
while True:
    n = int(input('Número: '))
    if n == 999:
        break  # interrompendo um laço infinito while True usando o break
    s += n
print(f'A soma vale: {s}')
