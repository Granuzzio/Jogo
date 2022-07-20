
# Error
    # Excelente p/ testes
    # Nao realiza o 'stop' no programa
    # Mensagem customizadas quando encontra um erro

'''
letras = ['a', 'b', 'c']
print(letras[2])

############################
try:
    letras = ['a', 'b', 'c']
    print(letras[6])
except IndexError:
    print('Esse index nao existe')
############################
'''

try:
    valor = int(input('Digite o valor do seu produto: '))
    print(valor)
except ValueError:
    print('Favor digitar um valor em numeros')
print('Continue seu codigo')
