
print('Seja bem vindo!\n')

num = int(input('Informe um número: '))

antigo_num = num

#UNIDADES
unidade = num % 10

#ELIMINAR A UNIDADE PARA ACHAR AS DEZENAS
num = (num - unidade) / 10

#DEZENA
dezena = num % 10

#ELIMINAR A UNIDADE PARA ACHAR AS CENTENAS
num = (num - dezena) / 10

#CENTENA
centena = num

dezena = int(dezena)
centena = int(centena)

print('O numero:',antigo_num,'tem:',unidade,'unidades','|',dezena,'dezenas','|',centena,'centenas')



