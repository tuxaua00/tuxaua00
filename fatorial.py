#PROGRAMA - CALCULO FATORIAL
import math
from math import factorial
import time

numero = int(input('Digite um número para o cálculo:\n'))

while numero:
    print('FATORIAL DE',numero,':',math.factorial(numero))
    if numero > 0:
        break
print('acabou!')
