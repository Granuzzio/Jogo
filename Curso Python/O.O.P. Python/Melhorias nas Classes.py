
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
     def nome_completo(self):
          return self.nome + ' ' + self.sobrenome

# Criar o objeto
usuario1 = Funcionarios('Elena', 'Cabral', '12/01/2009')
usuario2 = Funcionarios('Carol', 'Silva', '15/10/2005')
usuario3 = Funcionarios('Andre', 'Nascimento', '11/03/2003')

print(usuario1.nome_completo()) # OUTRA FORMA
print(Funcionarios.nome_completo(usuario1)) # Melhor Forma de escrever (melhor para ler)


"""
print(usuario1.nome + ' ' + usuario1.sobrenome)
print(usuario2.nome + ' ' + usuario2.sobrenome)   # fORMA MAIS DIFICIL
print(usuario3.nome + ' ' + usuario3.sobrenome)
"""