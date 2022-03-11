print('Seja bem vindo!\n')

lista = []

num = int(input('Informe o valor inicial da lista: '))
num2 = int(input('Informe o valor final da lista: '))

for i in range(num,num2):

    lista.append(i)

print('LISTA GERADA NO INTERVALO (',num,',',num2,'):')
print(lista)
