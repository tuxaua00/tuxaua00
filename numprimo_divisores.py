import time
#EU ACHO QUE NÃO FUNCIONA, MAS... SEGUE A LUTA!

print('Seja bem vindo!\n')

def divisores(num):
    for i in range(1, num//2+1):
        if num % i == 0:
            yield i
    yield num

num = int(input('Informe um número: '))

if num % 2 != 0 and num / 1 == num:
    print('Esse número é primo! NUMERO:',num)
else:
    print('Esse número não é primo! NUMERO:',num)
    print('E seus divisores são:',list(divisores(100)))