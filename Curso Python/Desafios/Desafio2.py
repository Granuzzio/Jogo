
# Desafio com Funcoes
'''
Criar um programa que calcula a quantidade de tintas necessarias para a pintar uma parede.
O usuario devera fornecer as seguintes informacoes:rendimento, altura e largura.
O programa deve mostrar na tela a mensagem 'Voce necessita de x latas de tintas'.
'''


rendimento = int(input("Qual o rendimento da lata? "))
altura = int(input("Qual a altura da parede? "))
largura = int(input("Qual a largura da parede? "))

def calculo_tinta():
    total = altura * largura / rendimento
    #print(f'A metragem da sua parede e de: {area}m2')
    print(f'E a quantidade de latas de tintas que voce ira precisar e de: {total} latas')
calculo_tinta()