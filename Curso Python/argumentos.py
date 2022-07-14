
# Funcoes
    # Varios Argumentos

#Criando um argumentos que soma varios numeros.
"""
def soma(*numeros):
    resultado = 0 # 0 e meu ponto de partida para a soma, comeco a somar 0 com o primeiro numero
    for num in numeros: # Esse loop faz o calculo em sequencia repetindo ate finalizar exemplo
        resultado += num  # Resultado = 0+ {num=numeros} 2= 2 e retorna o resultado 2 e volta a fazer o mesmo
    return resultado # resultado=2+num=3=5. 5+4=9. 9+7=16. termina


x = soma(2,3,4,7)
print(x)
"""
"""
def calculadora(*numeros):
    resultado = 1
    for num in numeros:
        resultado *= num
    return resultado
y=calculadora(1,2,3,4,5,6,7,8,9,10)
print(y)
"""

# Criando uma funcao que armazena numeros e strings (dados)

def agencia(**carro):
    return carro

print(agencia(marca='gol', cor='branca', motor=1.0, placa=123456))
print(agencia(marca='gol', cor='preta', motor=1.6,))
print(agencia(marca='gol', cor='azul', placa=132465))
print(agencia(marca='gol', cor='branca', motor=2.0, placa=654321))