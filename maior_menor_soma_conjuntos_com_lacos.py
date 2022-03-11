print('Seja bem vindo!\n')

num_inicio = int(input('Informe o número inicial do seu conjunto: '))
num_final = int(input('Informe o número final do conjunto: '))
lista = []

for i in range(num_inicio,num_final+1):
    lista.append(i)

print('\nCONJUNTO GERADO:',lista)

#SOMA DOS NUMEROS DO CONJUTO
soma_conjunto = sum(lista)
print('\nA SOMA DOS NUMEROS É:',soma_conjunto)

#MAIOR VALOR DO CONJUNTO
print('O maior valor do conjunto é:',max(lista))

#MENOR VALOR DO CONJUNTO
print('O menor valor do conjunto é:',min(lista))

