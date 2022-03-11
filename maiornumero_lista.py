print('Seja bem vindo!\n')

numeros = []

for num in range(1,7):
    numeros.append(int(input('Digite um número: ')))

maiorNumero = numeros[0]

cont = 1

while cont < len(numeros):
    if numeros[cont] > maiorNumero:
        maiorNumero = numeros[cont]
    cont = cont + 1

print('\nO maior número é:',maiorNumero)
