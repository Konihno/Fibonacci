def  fibonacci(n):

	if n == 1  or n == 0:

		return n

	else:

		return fibonacci(n-2) + fibonacci(n - 1)


nombre = int(input("Entre un chiffre/nombre positif: "))

if nombre < 0:
	print("Nombre non valide")

i = 0

print("Suite de fibonacci: ")

for i in range(0, nombre):
	print(fibonacci(i))