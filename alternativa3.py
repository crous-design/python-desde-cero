nota = int(input("Dime tu nota: "))
if nota >=1 and nota <= 4:
	print("Suspenso")
elif nota == 6 or nota == 7:
	print("Bien")
elif nota == 8:
	print("Notable")
elif nota == 9 or nota == 10:
	print("Sobresaliente")
else:
	print("Nota incorrect")
print("Programa finalziado")
