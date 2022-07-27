def calculadora (num1, num2, operacao):
	if(operacao == 1):
		res = num1+num2
	elif(operacao == 2):
		res = num1-num2
	elif(operacao == 3):
		res = num1*num2
	elif(operacao == 4):
		res = num1/num2
	else:
		res = 0
	return res

print("Bem-vindo! \n")
print("Que tipo de operação você quer realizar?")

operacao = int

while operacao != 0:
    operacao = int(input('Digite \n 1 para soma;\n 2 - subtração;\n 3 - multiplicação;\n 4 - divisão;\n 0 - sair\n:'))
    if(operacao == 0):
        break
    num1 = float(input('Digite o primeiro número:'))
    num2 = float(input('Digite o segundo número:'))
    print("\n")
    resultado = calculadora(num1, num2, operacao)
    print("O resultado esperado é = " + str(resultado))
    print("\n")

print("Até a próxima!")