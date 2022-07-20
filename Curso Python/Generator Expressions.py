from sys import getsizeof
# Generator Expressions
    # Uma forma mais rapida para listas, dicionarios e etc
    # Menos memoria alocada
    # Valores em bytes

numeros = [x * 10 for x in range(1000)]
print(type(numeros))
print(numeros)
print(getsizeof(numeros))
print()
print()
print()
numeros = (x * 10 for x in range(1000))
print(type(numeros))
print(list(numeros))
print(getsizeof(numeros))