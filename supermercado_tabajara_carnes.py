
def preco_file(f):

    preco_simples = 4.9
    preco_acima = 5.80
    vl_simples = (f*preco_simples)
    vl_acima = (f*preco_acima)
    vl_total = 0

    if f < 5:

        vl_total = (vl_simples)

    elif f > 5:

        vl_total = (vl_acima)

    return vl_total

def preco_alcatra(a):

    preco_simples = 5.9
    preco_acima = 6.8
    vl_simples = (a*preco_simples)
    vl_acima = (a*preco_acima)
    vl_total = 0

    if a < 5:

        vl_total = vl_simples

    elif a > 5:

        vl_total = vl_acima

    return vl_total

def preco_picanha(p):

    preco_simples = 6.9
    preco_acima = 7.8
    vl_simples = (p*preco_simples)
    vl_acima = (p*preco_acima)
    vl_total = 0

    if p < 5:

        vl_total = vl_simples

    elif p > 5:

        vl_total = vl_total

    return vl_total

def menu():

    print('Seja bem vindo!\n')
    print('Supermercado TABAJARA - Sexta da Carne\n')

    print('--- VALORES ---')
    print('FILE DUPLO - ATÉ 5KG: 4.90 R$ | ACIMA DE 5KG: 5.80 R$')
    print('ALCATRA - ATÉ 5KG: 5.90 R$ | ACIMA DE 5KG: 6.80 R$')
    print('PICANHA - ATÉ 5KG: 6.90 | ACIMA DE 5KG: 7.80 R$\n')

    print('Informe qual carne você deseja (somente uma)')
    cond = input('F PARA FILE DUPLO | A PARA ALCATRA | P PARA PICANHA\n')

    if len(cond) > 1:
        print('comando invalido, volte ao inicio!')
        exit(0)

    qtd = float(input('Quantos KGs você deseja: '))
    if cond.upper() == 'F':

        valor_total = preco_file(qtd)
        print('\nVocê pediu',qtd,'KG de FILE DUPLO')
        print('E irá pagar: {:.2f}'.format(valor_total))

    elif cond.upper() == 'A':

        valor_total = preco_alcatra(qtd)
        print('\nVocê pediu', qtd, 'KG de ALCATRA')
        print('E irá pagar: {:.2f}'.format(valor_total))

    elif cond.upper() == 'P':

        valor_total = preco_picanha(qtd)
        print('\nVocê pediu', qtd, 'KG de PICANHA')
        print('E irá pagar: {:.2f}'.format(valor_total))

menu()
