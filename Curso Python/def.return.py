
# Funcoes
    # DRY - Don't repeat youself.
    # Realizam uma tarefa
    # Calcula e retorna um valor

def cliente_1(nome):
    print(f'Ola {nome}')

def cliente_2(nome):
    return f'Ola {nome}'

x = cliente_1('Fabiana')
y = cliente_2('Fernando')

print(x)
print(y)
