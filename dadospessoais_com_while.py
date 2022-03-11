#ESTRUTURAS DE REPETIÇÃO

import datetime

#INICIO
print('Seja bem vindo!\n')

#NOME DA PESSOA
nome = input ('Informe seu nome: ')
while (len(nome) < 3):
    print('Nome tem que ter no minimo 3 caracteres! Informe novamente ')
    nome = input('Informe seu nome: ')
#FIM

#IDADE DA PESSOA
idade = int (input('Informe sua idade: '))
while (idade < 0) or (idade > 150):
    print('Idade Invalida! Informe novamente')
    idade = int(input('Informe sua idade: '))
#FIM

#SALARIO DA PESSOA
salario = int (input('Informe seu salário líquido: '))
while (salario < 0):
    print('Salario Inexistente! Por acaso, você deve o banco? Informe novamente')
    salario = int(input('Informe seu salário líquido: '))
#FIM

#SEXO DA PESSOA
print('INFORME SEU SEXO')
sexo = input('M PARA MASCULINO | F PARA FEMININO\n')
sx = ''

while (len(sexo) > 1):
    print('Sexualidade Inexistente! Informe uma válida')
    sexo = input('M PARA MASCULINO | F PARA FEMININO\n')

if sexo.upper() == 'M':
    sx = 'MASCULINO'
elif sexo.upper() == 'F':
    sx = 'FEMININO'
#FIM

#ESTADO CIVIL DA PESSOA
print('Informe seu estado cívil: SOLTEIRO(a) | CASADO(a) | VIUVO(a) | DIVORCIADO(a)')
estado_civil = input('S | C | V | D: ')
es = ''
condi = ('S','C','V','D')

while (len(estado_civil) > 1):
    print('Estado civil invalido! informe novamente')
    estado_civil = input('S | C | V | D: ')

if estado_civil.upper() == 'S':
    es = 'SOLTEIRO(a)'
elif estado_civil.upper() == 'C':
    es = 'CASADO(a)'
elif estado_civil.upper() == 'V':
    es = 'VIUVO(a)'
elif estado_civil.upper() == 'D':
    es = 'DIVORCIADO(a)'
#FIM

print('\n------ TABELA DE DADOS ------\n')

print('NOME:',nome.upper(),'|','IDADE:',idade,'|','SALARIO:',salario)
print('SEXO:',sx,'|','ESTADO CIVIL:',es,'\n')

print('Esse app foi utilizado em:',datetime.date.today())






