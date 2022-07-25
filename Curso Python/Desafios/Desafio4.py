# Calculadora de IMC - Indice de massa corporal

"""
Qual e a sua altura em cm?
Qual e o seu peso em kg?

Menor que 18,5  Magreza
Entre 18,5 e 24,9 Normal
Entre 25,0 e 29,9 Sobrepeso
Entre 30,0 e 39,9 Obesidade
Maior que 40,0 Obesidade grave
"""

altura = float(input('Qual e a sua altura (sem pontos ou virgula)? '))
peso = float(input('Qual o seu peso (sem pontos ou virgula)? '))
IMC = peso / (altura/100)**2

if IMC < 18.5:
    print('Voce esta muito magro')
elif IMC >= 18.5 and IMC < 24.9:
    print('Seu peso esta normal')
elif IMC >= 25.0 and IMC < 29.9:
    print('Voce esta com sobrepeso')
elif IMC >= 30.0 and IMC < 39.9:
    print('Voce esta com inicio de obsidade')
else:
    print('Voce esta com obsidade grave')

"""
def imc():
   total = peso * peso / altura
   print(f'Seu IMC e: {total}')

imc()
"""