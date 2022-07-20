
# Error
    # Excelente p/ testes
    # Nao realiza o 'stop' no programa
    # Mensagem customizadas quando encontra um erro


try:
    valor = int(input('Digite o valor do seu produto: '))
    print(valor)
except ValueError:
    print('Favor digitar um valor em numeros')
finally:
    print('Codigo ok')
