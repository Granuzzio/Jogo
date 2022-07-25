# Desafio vom if, elif, else

"""
Criar um programa que dependendo da temperatura (em Celsius) do steak ele retorna o ponto de cozimento
em portugues. O ususario devera fornecer a temperatura.

Temperatura - Cozimento
120*F ou 48*C - Rare (Selado)
130*F ou 54*C - Medium rare (Ao ponto para o mal passado)
140*F ou 60*C - Medium (Ao ponto)
150*F ou 65*C - Medium well (Ao ponto para o bem passado)
160*F ou 71*C - Well done (Bem passado)
"""

temperatura = int(input('Qual a temperatura (Em Celsius) da carne? '))

if temperatura < 48:
    print('Cozinhar por mais tempo')
elif temperatura in range(48, 53):
    print('Selada')
elif temperatura in range(54, 59):
    print('Ao ponto para o mal passado')
elif temperatura in range(60, 64):
    print('Ao ponto')
elif temperatura in range(65, 70):
    print('Ao ponto para o bem passado')
elif temperatura >= 70:
    print('Bem passado')
