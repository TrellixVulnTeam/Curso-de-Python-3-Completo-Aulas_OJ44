a = input('\033[1mDigite algo:\033[m ')
print(f'\033[4;31mSó\033[m \033[4;31mtem\033[m \033[4;31mespaços\033[m\033[1m?\033[m \033[1;31;43m{a.isspace()}\033[m')
print(f'\033[31mÉ númerico??\033[m \033[1m{a.isnumeric()}\033[m')
print(f'\033[32mÉ somente alfabético???\033[m \033[1;4m{a.isalpha()}\033[m')
print(f'\033[33mÉ somente AlfaNúmerico??\033[m \033[1m{a.isalnum()}\033[m')
print(f'\033[34mEstá em LETRAS MAIUSCULAS????\033[m \033[1m{a.isupper()}\033[m')
print(f'\033[35mEstá em letras minúsculas???\033[m \033[4;1m{a.islower()}\033[m')
print(f'\033[35mEstá Capitalizada??\033[m \033[1;31;45m{a.istitle()}\033[m')

# --------------------------------------------------------------------------

a = input('\033[45m\n\033[m\033[1;4mDigite\033[m \033[1;4mALGO:\033[m ')
print(f'\033[7;47;30mSó tem ESPAÇOS?\033[m \033[1;31m{a.isspace()}\033[m')
print(f'\033[1mÉ \033[31mNUMERICO?\033[m \033[31;40m{a.isnumeric()}\033[m')
print(f'\033[7mÉ alfabético?\033[m \033[1;4m{a.isalpha()}\033[m')
print(f'\033[1mÉ alfanumérico? \033[32m{a.isalnum()}\033[m')
print(f'\033[7;33;44mÉ somente maiúsculo?\033[m \033[1;35m{a.isupper()}\033[m')
print(f'\033[1mÉ somente minúsculo? \033[31m{a.islower()}\033[m')
print(f'\033[1;4;33;44mÉ Capitalizada???\033[m \033[1m{a.istitle()}')

# --------------------------------------------------------------------------

a = input('Digite algo: ')
print(f'\n Só tem espaços? {a.isspace()}')
print(f'\n É numérico? {a.isnumeric()}')
print(f'\n É alfabético? {a.isalpha()}')
print(f'\n É alfanumérico? {a.isalnum()}')
print(f'\n É somente maiúsculo? {a.isupper()}')
print(f'\n É somente minúsculo? {a.islower()}')
print(f'\n Está capitalizada? {a.istitle()}')
