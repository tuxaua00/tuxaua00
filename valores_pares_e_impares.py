print('Seja bem vindo!\n')

lista = []
lista2 = []
lista3 = []
for i in range(10):
    lista.append(int(input('Digite um número: ')))

for valor in lista:

    if valor % 2 == 0:
        lista2.append(valor)
    else:
        lista3.append(valor)

print('\n',lista)
print('VALORES PARES:', lista2,'AO TOTAL DE:',len(lista2),'NUMEROS')
print('VALORES IMPARES:', lista3,'AO TOTAL DE:',len(lista3),'NUMEROS')





