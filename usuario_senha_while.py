#ESTRUTURAS DE REPETIÇÃO

print('Seja bem vindo!\n')

usuario = input('Informe seu login: ')
senha = input('Informe sua senha: ')

while (senha == usuario):
    print('Comando inválido, tente novamente!')
    usuario = input('Informe seu login: ')
    senha = input('Informe sua senha: ')

print('\nAgora tá certo!')






