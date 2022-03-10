import sys

def descontos_alcool(x):
    #SOMENTE ALCOOL
    preco = 1.90
    vl_pagar = 0
    valor_normal = (x * preco)

    if x <= 20:
        vl_pagar = (valor_normal-(valor_normal*(3/100)))
    elif x > 20:
        vl_pagar = (valor_normal - (valor_normal * (5 / 100)))

    return vl_pagar

def descontos_gasolina(z):
    #SOMENTE GASOLINA
    preco = 2.50
    vl_pagar = 0
    valor_normal = (x * preco)

    if x <= 20:
        vl_pagar = (valor_normal-(valor_normal*(4/100)))
    elif x > 20:
        vl_pagar = (valor_normal - (valor_normal * (6 / 100)))

    return vl_pagar

def menu():

    print('Seja bem vindo!\n')

    print('Posto de Gasolina\n')

    print('O que deseja? ALCOOL ou GASOLINA?')
    cond = input('Digite A para Alcool | G para GASOLINA: ')
    if len(cond) > 1:
        print('Valor invalido, volte ao inicio!')
        exit(1)
    qtd = float(input('Quantos litros você quer: '))
    if qtd < 0 or qtd > 290:
        print('valor informado invalido! volte ao inicio')
        exit(1)

    elif cond == 'A':
    preco_final = descontos_alcool(qtd)
    print('Valor total a ser pago em',qtd,'L de ALCOOL: {:.2f}'.format(preco_final))

    elif cond == 'G':
    if qtd < 0 and qtd > 290:  # PEGUEI BASE NO TANQUE DE COMBUSTIVEL DE UM CARRO DE LUXO
        print('valor informado invalido! volte ao inicio')
        exit(1)
    preco_final = descontos_gasolina(qtd)
    print('Valor total a ser pago em', qtd, 'L de GASOLINA: {:.2f}'.format(preco_final))

menu()

