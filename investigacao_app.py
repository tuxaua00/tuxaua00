def suspeitas(a,b,c,d,e):

    somatorio = (a+b+c+d+e)
    resultado = ''

    if somatorio == 2:
        resultado = 'SUSPEITO(A)'
    elif somatorio >= 3 and somatorio <= 4:
        resultado = 'CÚMPLICE'
    elif somatorio == 5:
        resultado = 'ASSASSINO'
    else:
        resultado = 'INOCENTE *_*'

    return resultado

def menu():

    print('Seja bem vindo!\n')
    print('INVESTIGAÇÃO DE HOMICIDIO')

    cont1, cont2, cont3, cont4, cont5 = 0, 0, 0, 0, 0

    print('1° - Você telefonou para a vítima?')
    resp1 = input('S/N: ')
    if len(resp1.upper()) > 1:
        print('Valor informado invalido, volte ao inicio!')
        exit(1)
    elif resp1.upper() == 'S':
        cont1 = 1

    print('2° - Esteve no local do crime?')
    resp2 = input('S/N: ')
    if len(resp2) > 1:
        print('Valor informado invalido, volte ao inicio!')
        exit(1)
    elif resp2.upper() == 'S':
        cont2 = 1

    print('3° - Mora perto da vítima?')
    resp3 = input('S/N: ')
    if len(resp3) > 1:
        print('Valor informado invalido, volte ao inicio!')
        exit(1)
    elif resp3.upper() == 'S':
        cont3 = 1

    print('4° - Devia para a vítima?')
    resp4 = input('S/N: ')
    if len(resp4) > 1:
        print('Valor informado invalido, volte ao inicio!')
        exit(1)
    elif resp4.upper() == 'S':
        cont4 = 1

    print('5° - Já trabalhou com a vítima?')
    resp5 = input('S/N: ')
    if len(resp5) > 1:
        print('Valor informado invalido, volte ao inicio!')
        exit(1)
    elif resp5.upper() == 'S':
        cont5 = 1

    print(cont1, cont2, cont3, cont4, cont5)

    resultado = suspeitas(cont1,cont2,cont3,cont4,cont5)

    print('\nApós uma análise, foi classificado que você é:',resultado)

menu()