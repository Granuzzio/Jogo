"""
for numero1 in range(1,6):
    print('produto ' + str(numero1))
    for numero2 in range(6):
        print(numero1, numero2)

"""

#  for loop nested

    #outer loop
    #inner lopp

# Modificar uma PALAVRA junta em uma P A L A V R A com espacamento.
"""
palavra = 'Fernando Granuzzio Fascirolli'

for espaco in palavra:
    print(f' {espaco}', end='')
"""

linhas = 6
colunas = 6
simbolos = '#'

for l in range(linhas):
    for c in range(colunas):
        print(simbolos, end='')
    print()
