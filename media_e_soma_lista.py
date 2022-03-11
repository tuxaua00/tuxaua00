print('Seja bem vindo!\n')

numeros = []

for num in range(8):
    numeros.append(int(input('Digite um número para a lista: ')))

soma_lista = sum(numeros)
media_lista = soma_lista/8
print('Lista:',numeros)
print('\nSoma dos números da lista:',soma_lista)
print('Média dos números da lista:',media_lista)

