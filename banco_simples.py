import sys

def menu():

    print('Seja bem vindo!\n')

    x = int(input('Informe o valor que deseja sacar: '))
    if x < 10:
        print('O valor mínimo para saque é 10R$, volte ao começo!')
        exit(1)
    if x > 600:
        print('O valor máximo para saque é 600R$, volte ao começo!')
        exit(1)

    dinheiro_total = x

    notas_cem = int(x / 100)
    x = x - (notas_cem * 100)

    notas_ciquenta = int(x / 50)
    x = x - (notas_ciquenta * 50)

    notas_dez = int(x / 10)
    x = x - (notas_dez * 10)

    notas_cinco = int(x / 5)
    x = x - (notas_cinco * 5)

    moeda_um = int(x / 1)
    x = x - (moeda_um * 1)

    print('Dinheiro solicitado: ',dinheiro_total)
    print('   Notas disponíveis  \n')
    print(notas_cem,'de 100R$','|',notas_ciquenta,'de 50R$','|',notas_dez,'de 10R$')
    print(notas_cinco,'de 5R$','|',moeda_um,'moedas de 1R$')

menu()


