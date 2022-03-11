#ESTRUTURAS DE REPETIÇÃO

print('Seja bem vindo!\n')

anos = 0

#POPULAÇÃO A
pop_a = int(input('Informe a população do municipio A: '))
taxa_a = float(input('Informe a % de crescimento anual:'))
while (taxa_a < 0) or (taxa_a > 100):
    print('Porcentagem invalida! informe novamente')
    taxa_a = float(input('Informe a % de crescimento anual:'))
taxa_a = taxa_a/100

#POPULAÇÃO B
pop_b = int(input('Informe a população do municipio B: '))
taxa_b = float(input('Informe a % de crescimento anual:'))
while (taxa_b < 0) or (taxa_b > 100):
    print('Porcentagem invalida! informe novamente')
    taxa_b = float(input('Informe a % de crescimento anual:'))
taxa_b = taxa_b/100

while (pop_a < pop_b):

    anos += 1
    pop_a = (pop_a+(pop_a*taxa_a))
    pop_b = (pop_b+(pop_b*taxa_b))
    #FIM DO WHILE

print('\nSe passou',anos,'anos até a população do municipio A ultrapassar o B!')
print('População atual do municipio A: {:.1f}'.format(pop_a))
print('População atual do municipio B: {:.1f}'.format(pop_b))







