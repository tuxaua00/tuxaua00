# LISTA DE EXERCICIO - PYTHON INICIANTE
#9
import datetime

print('CONVERSOR DE FAHRENHEIT PARA CELSIUS')

fah = int(input('Informe a temperatura em fahrenheit: '))
formula = (5*((fah-32)/9))

print('\n')
print('Temperatura em Celsius (C°):',formula)

print('\n')
print('Essa aplicação foi utilizada em: ',datetime.date.today())
