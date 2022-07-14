 # Funcoes
    # Paramentros --> Argumento


def boas_vindas(nome, quantidade): # nome e quantidade sao argumentos
    print(f'Ola {nome}.')
    print(f'Temos {str(quantidade)} de laptops em estoque')

boas_vindas('Marcos', 5)
boas_vindas('Fernando', 4)
boas_vindas('Fabiana', 2)

# Pode ser feita dos dois jeitos, mais o primeiro e mais curto

"""

def boas_vindas_Marcos():
    print('Ola Marcos')
    print('Temos 5 laptops em estoque')

def boas_vindas_Fernando():
    print('Ola Fernando')
    print('Temos 4 laptops em estoque')

def boas_vindas_Fabiana():
    print('Ola Fabiana')
    print('Temos 2 laptops em estoque')

boas_vindas_Marcos()
boas_vindas_Fernando()
boas_vindas_Fabiana()

"""