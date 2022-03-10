def par_impar(x):

    cd = ''

    if x % 2 == 0:
        cd = 'PAR'
    else:
        cd = 'IMPAR'

    return cd

def posi_nega(x):

    cd = ''

    if x > 0:
        cd = 'POSITIVO'
    else:
        cd = 'NEGATIVO'

    return cd

def int_dec(x):

    cd = ''

    if (x // 1 == x):
        cd = 'INTEIRO'
    else:
        cd = 'DECIMAL'

    return cd

def menu():

    print('seja bem vindo!\n')

    num = float(input('Informe um número: '))

    p_i = par_impar(num)
    p_n = posi_nega(num)
    i_d = int_dec(num)

    print('\nO número:',num,'é:',p_i,'|',p_n,'|',i_d)

menu()

