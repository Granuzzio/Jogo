
# Sets (Listas)
    # Similar a listas
    # Evita itens duplicados
    # Nao utiliza index (perde)

list1 = [10, 20, 30, 40, 50]
list2 = [10, 20, 60, 70]

num1 = set(list1)
num2 = set(list2)

print(num1 | num2) # Union
print()
print(num1 - num2) # difference
print()
print(num1 ^ num2) # Symmetric Difference
print()
print(num1 & num2) # And

print(len(num1))

