
# List Comprehension
    # Mais simples de escrever
    # Utilizado quando voce precisar criar uma nova lista a partir de uma existente
    # [Expressao for item in itens]

frutas1 = ['abacate', 'banana', 'morango', 'kiwi', 'abacaxi']
#frutas2 = []

#for iten in frutas1:
#    if 'n' in iten:
#        frutas2.append(iten)

frutas2 = [iten for iten in frutas1 if 'k' in iten]

print(frutas2)