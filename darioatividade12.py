 # Exercício Python 12: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
ano = int(input("digite o ano:"))
if ano % 100 != 0 and ano % 4 == 0 or ano % 400 == 0:
    print("o ano é bisexto:)")
else:
    print("não é bisexto:(")