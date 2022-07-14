# Dicionarios
    # Utiliza index no formato de keys e values
    # Aceita string, integer, floot, boolean...

aluno = {'nome': 'Ana', 'idade': 16, 'nota_final': 'A', 'aprovacao': True}
#     Keys /\      /\ values
"""
print(aluno['nome'])
aluno['nome'] = 'Jose' # da para alterar apenas um item no dicionario
print(aluno['nome'])
aluno.update({'nome': 'Maria', 'nota_final': 'B'}) #da para alterar mais itens no dicionario
print(aluno)
"""
aluno.update({'endereco': 'Rua Equador'}) # se nao tiver o item, ele e adicionado ao final
print(aluno.get("endereco", 'Nao existe')) # Nao existe mais nao gera um erro e consigo digita o valor
del aluno['idade']
print(aluno)