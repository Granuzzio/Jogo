


#for numero in range(6):
#    print(numero)

"""
palavra = 'Espetacular'

for letra in palavra:
    print(f'{letra} esta dentro da palavra {palavra}')
"""

compra_confirmada = False # (muda conforme falso ou verdadeiro)
dados_compra = 'Compra no valor de 120.00 realizada com sucesso'

for enviar in range(3):
    if compra_confirmada:
        print(dados_compra)
        print('Compravante enviado para o seu email!')
        break
else:
    print('Falha na compra')