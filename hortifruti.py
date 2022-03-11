import sys

def preco_morango(x):

    vl_total = 0
    preco_simples = 2.5
    preco_acima = 2.2
    vl_compra_simples = (preco_simples*x)
    vl_compra_acima = (preco_acima*x)

    if x <= 5:

        vl_total = (vl_compra_simples)

    elif x > 5:

        vl_total = (vl_compra_acima)

    return vl_total

def preco_maca(m):

    vl_total = 0
    preco_simples = 1.8
    preco_acima = 1.5
    vl_compra_simples = (preco_simples * m)
    vl_compra_acima = (preco_acima * m)

    if m <= 5:

        vl_total = (vl_compra_simples)

    elif m > 5:

        vl_total = (vl_compra_acima)

    return vl_total

def menu():

    print('Seja bem vindo!\n')
    print('Hortifruti do Papizão!\n')

    print('FRUTAS DISPONÍVEIS: MORANGO | MAÇA')
    cond = input('DIGITE A PARA MORANGO | M PARA MAÇA | D PARA COMPRAR OS DOIS\n')

    if len(cond) > 1:
        print('comando invalido, volte ao inicio!')
        exit(0)

    if cond.upper() == 'A':
        print('\n')
        qtd = int(input('Quantos KGs de morango: '))
        preco_final = preco_morango(qtd)
        print('Você comprou',qtd,'KG de morango')
        print('Pelo preço de:',preco_final,'R$')

    elif cond.upper() == 'M':
        print('\n')
        qtd = int(input('Quantos KGs de maça: '))
        preco_final = preco_maca(qtd)
        print('Você comprou', qtd, 'KG de maça')
        print('Pelo preço de:', preco_final, 'R$')

    elif cond.upper() == 'D':
        print('\n')
        qtd = int(input('Quantos KGs de morango: '))
        qtd_2 = int(input('Quantos KGs de maça: '))

        soma1 = (qtd+qtd_2)
        soma2 = preco_morango(qtd) + preco_maca(qtd_2)

        if soma1 >= 8 or soma2 >= 25:

            soma_total = (soma2-(soma2*(10/100)))
            print('\nKG de MORANGO:',qtd,'|','KG de MAÇA:',qtd_2)
            print('Valor total do morango: {:.2f}'.format(preco_morango(qtd)),'R$')
            print('Valor total da maça: {:.2f}'.format(preco_maca(qtd_2)),'R$')
            print('Valor do desconto: {:.2f}'.format(soma2*(10/100)),'R$')
            print('Valor total dos produtos: {:.2f}'.format(soma_total),'R$')

menu()

