try:
    a = int(input('numerador: '))
    b = int(input('denominador: '))

    r = a / b

# except (ValueError, TypeError):
#     print('\033[91mTivemos problemas com os tipos de dados que você informou!\033[m')

except ZeroDivisionError:
    print('\033[91mDivisão por 0 não é possivel!\033[m')

except KeyboardInterrupt:
    print('\033[91mO usuário não entrou com nenhum dado!\033[m')

except Exception as erro:
    print(f'A classe do erro foi {erro.__class__}')

else:
    print(f'Resultado {r:.1f}')

finally:
    print('Volte sempre! Muito obrigado!')

# except Exception as erro:
#     print(f'\033[91mO problema encontrado foi\n{erro.__class__}\033[m')