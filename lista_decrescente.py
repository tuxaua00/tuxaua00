
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import sys
import math


print('Seja bem vindo!\n')

x = int(input('Digite o 1° NUMERO: '))
y = int(input('Digite o 2° NUMERO: '))
z = int(input('Digite o 3° NUMERO: '))

lista_n = [x,y,z]
print('\nLista na ordem original: ',lista_n)

lista_n.sort(reverse = True)
print('Lista na ordem decrescente: ',lista_n)

