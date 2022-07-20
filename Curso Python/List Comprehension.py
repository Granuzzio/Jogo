
# List Comprehension
    # Mais simples de escrever
    # Utilizado quando voce precisar criar uma nova lista a partir de uma existente
    # [Expressao for item in itens]

#valores = []

#for x in range(6):
#    valores.append(x * 10)

valores = [x * 10 for x in range(6)]

print(valores)