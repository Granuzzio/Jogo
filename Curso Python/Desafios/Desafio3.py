# Desafio com 'Sets'

"""
Criar um programa que gera 3 Listas de acordo com a necessidade logo abaixo:

Lista1 = Funcionario que tem carro e trabalham durante a noite
Lista2 = Funcionario que tem carro e trabalham durante o dia
Lista3 = Funcionario que nao tem carro
"""
funcionarios = ['Ana', 'Marcos', 'Alice', 'Pedro', 'Sophia', 'Bruno', 'Melissa']
turno_dia = ['Ana', 'Marcos', 'Alice', 'Melissa']
turno_noite = ['Pedro', 'Sophia', 'Bruno']
tem_carro = ['Marcos', 'Alice', 'Bruno', 'Melissa']



lista1 = set(tem_carro).intersection(turno_noite)
print(lista1)
lista2 = set(tem_carro).intersection(turno_dia)
print(lista2)
lista3 = set(funcionarios).difference(tem_carro)
print(lista3)


"""
set4 = set3.difference(set1) Faz a diferenca de um para o outro
#set4 = set1.intersection(set2)

print(num1 | num2) # Union
print()
print(num1 - num2) # difference
print()
print(num1 ^ num2) # Symmetric Difference
print()
print(num1 & num2) # And

"""