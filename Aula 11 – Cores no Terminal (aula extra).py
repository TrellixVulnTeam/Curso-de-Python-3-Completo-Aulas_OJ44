# \033[0;30;41m
# \033[4;33;44m
# \033[1;35;43m
# \033[30;42m
# \033[m
# \033[7;30m]
print('\033[1;31mCurso em Vídeo PYTHON!.\033[m')
name = 'Davyd Kennedy'
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7;30m',
         'negrito': '\033[1m'
         }

print(f'Olá! Muito prazer em te conhecer, \033[1;31m{name}\033[m')
print(f'Olá, Muito prazer em te conhecer, {cores["azul"]}{name}{cores["limpa"]}')  # usar aspas duplas para o que está dentro de CHAVES.
print(f'Olá, {cores["amarelo"]}{cores["negrito"]}{name}{cores["limpa"]}, é muito bom te conhecer!')
print('Olá, Muito prazer em te conhecer, {}{}{}'.format(cores['pretoebranco'], name, cores['limpa']))
