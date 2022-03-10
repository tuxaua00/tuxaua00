
print('Seja bem vindo!\n')

ano = int(input('Informe o ano que você nasceu: '))

if (ano % 4 == 0) != (ano % 100 == 0):

    print('O ano',ano,'é um ano bissexto!')

else:

    print('O ano',ano,'não é um ano bissexto!')

