
#  Filter Function
    # Muito utilizado com listas
    # Aplicar uma funcao a um interable, filtrando os itens. (list, tuple, dic, etc.)


Valores = [10, 12, 34, 44, 57]

def remover20(x):
    return x > 20

#print(list(map(remover20, Valores))) mostra True or False
print(list(filter(remover20, Valores))) # tira todo numero abaixo de 20
print(list(filter(lambda x: x > 20, Valores)))
