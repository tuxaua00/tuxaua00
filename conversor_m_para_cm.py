# LISTA DE EXERCICIO - PYTHON INICIANTE
#5
import datetime

print('CONVERSOR DE METROS PARA CENTIMETROS\n')

num_metro = float(input('Informe o número em metros'))
conversor = (num_metro*100)

print('A CONVERSÃO DO NUMERO,',num_metro,'DE M PARA CM É:{:.2f}'.format(conversor))

print('Essa aplicação foi utilizada em: ',datetime.date.today())
