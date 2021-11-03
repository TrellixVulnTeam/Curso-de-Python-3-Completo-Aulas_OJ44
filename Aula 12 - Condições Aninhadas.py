import emoji
# ALT+205 ═
# ALT+201 ╔
# ALT+187 ╗
# ALT+188 ╝
#  alt + 219 █
# alt + 220 ▄
# ALT+200 ╚
# --------------------------------------------------------------------------

print('\033[1;94m-=-\033[m' * 18,
      '\n\033[97m               Condições Aninhadas'
      )
print('\033[1;94m-=-\033[m' * 18, '\n')




name = str(input('\033[97m  Informe o seu nome, por favor: ')).strip().lower()
if name.upper() == 'DAVYD':
    print(f'\n  Olá, {name}\n'
          f'  {name} com Y é foda né meu parceiro!? ')

elif name.upper() == 'Pedro'.upper() or name == 'Tiago'.upper() or name == 'João'.upper():
    print('\n  O seu nome é muito popular no nosso país.')

elif name.lower() in 'sonally cecília ana maria socorro':
    print('\n  Este é um belo nome feminino!')

elif name.lower() in 'abél caim castiel chuck jack nabucodonozor':
    print(emoji.emojize('\n  Supernatural! :fire:', use_aliases=True))

else:
    print('\n  Seu nome é bem normal! Tenha um bom dia.')


# --------------------------------------------------------------------------


# nome = str(input('Qual é o seu nome? '))
# if nome == 'Davyd':
#     print(f'Olá,\033[1;31m{nome}\033[m!')
# elif nome == 'zé' or nome == 'ze' or nome == 'Maria' or nome == 'Paulo':
#     print('\n\033[31mSeu nome é muuuito popular no BRASIL!')
# elif nome in 'Ana Cláudia Jéssica Juliana Sonally Cecilia':
#     print('\n\033[1;35mEste nome é feminino.\033[m')
# elif nome in 'joão abél caim castiel chuck':
#     print(emoji.emojize('\nSUPERNATURAL! :fire: ', use_aliases=True))
# else:
#     print('\nSeu nome é bem normal.\n\n  \033[1;4mTenha um bom dia.\033[m')

# --------------------------------------------------------------------------
