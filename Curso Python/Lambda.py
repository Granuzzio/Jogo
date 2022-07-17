
# Lambda Function
    # E um funcao (pequena) sem nome
    # Pode ter varios argumentos mas somente uma expressao
    # Muito utilizada dentro de outras funcoes
    # Codigo mais 'Clean'

"""
#def somar(x):
#    return x+10
#print(somar(3))

somar10 = lambda x,y: x + y + 10
print(somar10(2,4))
"""

def somar(x):
    func2 = lambda x: x + 10
    return func2(x) * 4
print(somar(2))






