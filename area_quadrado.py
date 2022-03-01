# LISTA DE EXERCICIO - PYTHON INICIANTE
#7
import datetime

print('CALCULO DE AREA DO QUADRADO + O DOBRO DA MESMA\n')

quadrado = int(input('Informe o valor do lado do quadrado: '))
area_q = (quadrado**2)
dobro_area = (area_q*2)

print('A área do quadrado é:',area_q,'e o seu dobro é:',dobro_area)

print('\n')
print('Essa aplicação foi utilizada em: ',datetime.date.today())
