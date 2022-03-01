# LISTA DE EXERCICIO - PYTHON INICIANTE
#4
import datetime

print('CALCULADORA DE MÉDIA ANUAL PARA APROVAÇÂO EM ANO LETIVO\n')


nome = input('Informe seu nome:')
num1 = int(input('Informe a média do 1° BIM:'))
num2 = int(input('Informe a média do 2° BIM:'))
num3 = int(input('Informe a média do 3° BIM:'))
num4 = int(input('Informe a média do 4° BIM:'))
print('\n')
media_anual = ((num1+num2+num3+num4)/4)

if media_anual >= 7 and media_anual <=10:
    print('Parabéns',nome,'você foi APROVADO com média: {:.2f}\n'.format(media_anual))
elif media_anual < 7 and media_anual >= 5:
    print('Você,',nome,',está de RECUPERAÇÃO e com média: {:.2f}\n'.format(media_anual))
else:
    print('Você,',nome,",está REPROVADO e com média: {:.2f}\n".format(media_anual))

print('Esse aplicativo foi usado em: ',datetime.date.today())

