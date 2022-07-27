'''import time

tempoInicial = 60
tempoFinal = 0

print("Iniciando contagem regressiva!")

for i in range(tempoInicial, tempoFinal, -1):
	print(i)
	time.sleep(1)

print("BUM!")'''


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

num1 = 10
num2 = 4
operacao = 1
resultado = calculadora(num1, num2, operacao)
print(resultado)