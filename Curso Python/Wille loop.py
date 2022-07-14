# Excelente para loops dependentes de uma condicao
# Cria uma promocao para um produto no valor de R$ 100.
"""
valor = 100
dia = 0
while valor > 20:
    dia += 1
    print(f' No dia {dia} o produto vai ser vendido por R${valor}')
    valor -= 5
"""

valor = int(input('Qual e o valor R$ do produto? '))

while valor > 20:
    valor = (valor * 0.10) + valor
    print(f'O valor final do seu produto sera de R${valor}')
    break






