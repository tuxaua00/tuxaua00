import numpy as np

#NÃO MEXA NO CODIGO, ESTÁ FUNCIONANDO MAS NÃO SEI COMO! '-'

def tp_triangulo(x,y,z):

    tipo_triangulo = ''

    if x == y and z:

        tipo_triangulo = 'TRIANGULO EQUILÃTERO'

    elif x == y or x == z or y == z:

        tipo_triangulo = 'TRIANGULO ISÓCELES'

    elif x != y and z != x and y:

        tipo_triangulo = 'TRIANGULO ESCALENO'

    return tipo_triangulo

def forma_trian(x,y,z):

    f = ''

    if x+y > z or x+z > y or y+z > x:

        f = 'S'

    else:

        f = 'N'

    return f

def menu():

    print('Seja bem vindo!\n')

    lado1 = int(input('Informe o lado esquerdo do triangulo: '))
    lado2 = int(input('Informe o lado direito do triangulo: '))
    base = int(input('Informe o lado da base do triangulo: '))

    if forma_trian(lado1,lado2,base) == 'S':

        print('\nPode ser formado um',tp_triangulo(lado1,lado2,base))
        print('Com lados:',lado1,'|',lado2,'|',base)

    elif forma_trian(lado1,lado2,base) == 'N':

        print('\nNão pode ser formado nenhum tipo de triangulo!')

menu()


