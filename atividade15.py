# Crie um programa que receba dois números e uma operação (soma, subtração, multiplicação ou divisão) e execute a operação desejada.

numero1 = float(input("insira um numero: "))
operacao =(input("insira a operação: "))
numero2 = float(input("insira outro numero: "))

if operacao == "+":
    result = numero1 + numero2
    print(F"o resultado é: {result}")

elif  operacao == "*":
    result = numero1 * numero2
    print(F"o resultado é: {result}")

if operacao =="/":
    result = numero1 / numero2
    print(F"o resultado é: {result}")

elif operacao == "-":
    result = numero1 - numero2
    print(F"o resultado é: {result}")