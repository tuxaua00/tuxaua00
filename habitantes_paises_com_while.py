#ESTRUTURAS DE REPETIÇÃO

pop_a = 80000
pop_b = 200000
anos = 0
taxa_a = 3/100
taxa_b = 1.5/100

while (pop_a < pop_b):
    anos += 1
    pop_a = pop_a+(pop_a*taxa_a)
    pop_b = pop_b+(pop_b*taxa_b)

print('Após', anos, 'Anos o País A ultrapassou B')
print('HABITANTES PAIS A: {:.1f}'.format(pop_a))
print('HABITANTES PAIS B: {:.1f}'.format(pop_b))



