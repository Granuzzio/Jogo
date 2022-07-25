# Sets (Lista)
    # Similar a Lista
    # Evita itens duplicados


set1 = {'a', 'b', 'c'}
set2 = {'a', 'd', 'e'}
set3 = {'c', 'd', 'f'}

#set4 = set1.union(set2)# Une as duas listas sem repetir
set4 = set3.difference(set1)# Faz a diferenca de um para o outro
#set4 = set1.intersection(set2)# O que tem em um que tem no outro
#set4 = set1.symmetric_difference(set2)# Nao mostra tudo o que estiver duplicado


print(set4)