
    # Python Object - Oriented  Programming

# Classes
    # Utilizada para criar objetos (Instances)
    # Objetos sao partes dentro de uma class (Instances)
    # Classes sao utilizadas para agrupar dados e funcoes, podendo reutilizar
    # ====
    # Class: Frutas
    # Objects: Abacate, Banana...

# Criar a classe
class Funcionarios:
     def __init__(self, nome, sobrenome, data_nascimento):# Self e o objeto(usuario1) e o nome... e o argumento
          self.nome = nome
          self.sobrenome = sobrenome
          self.data_nascimento = data_nascimento

# Criar o objeto
usuario1 = Funcionarios('Elena', 'Cabral', '12/01/2009')
usuario2 = Funcionarios('Carol', 'Silva', '15/10/2005')
usuario3 = Funcionarios('Andre', 'Nascimento', '11/03/2003')

print(usuario1.nome)
print(usuario2.nome)
print(type(usuario3))
"""
# Criar os parametros do usuario1
usuario1.nome = 'Elena'
usuario1.sobrenome = 'Cabral'
usuario1.data_nascimento = '12/01/2009'

# Criar os parametros do usuario2
usuario2.nome = 'Carol'
usuario2.sobrenome = 'Silva'
usuario2.data_nascimento = '12/01/2005'


# print
print(usuario1.nome)
print(usuario2.nome)
"""