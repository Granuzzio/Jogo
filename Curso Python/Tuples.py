# Tuples
    # Armazenar mais de uma informacao em uma variavel
    # Manter a sequencia de dados em uma variavel
    # Nao podem ser alterados (Immutable)


cores_list = ['amarelo', 'verde', 'azul', 'vermelho']
cores_tuple = ('amarelo', 'verde', 'azul', 'vermelho')

# cores_list.append('Roxo') Adiciona a lista (isso e permitido)
# cores_tuple.append('roxo') nao e permitido adicionar nada a uma tuple

print(type(cores_list))
print(type(cores_tuple))

duas_listas = cores_list * 2
print(duas_listas)