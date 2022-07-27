#FUNÇÃO PARA FAZER AS QUATRO OPERAÇÕES COM DOIS NUMEROS

from ntpath import realpath


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
print("Que tipo de operação você quer realizar?\n")
operacao = int(input('Digite (1 - soma; 2 - subtração; 3 - multiplicação; 4 - divisão) :'))
num1 = float(input('Digite o primeiro número:'))
num2 = float(input('Digite o segundo número:'))
resultado = calculadora(num1, num2, operacao)
print("O resultado esperado é = " + str(resultado))