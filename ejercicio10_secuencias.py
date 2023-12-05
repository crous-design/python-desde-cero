#Diseñar el algoritmo correspondiente a un programa, que:

#Crea una tabla (lista con dos dimensiones) de 5x5 enteros.
#Carga la tabla con valores numéricos enteros.
#Suma todos los elementos de cada fila y todos los elementos de cada columna visualizando los resultados en pantalla.

tabla = []
for indice_file in range(1,6):
	fila = []
	for indice_col in range(1,6):
		fila.append(int(input("Introduce un numero de la fila %d y columna %d:")))
	tabla.append(fila)

indice_file = 1
for fila in tabla:
	print("La suma de los elementos de la fila %d es %d" % (indice_fila,sum(fila)))
	indice_fila += 1

#SUma las columnas
for indice_col in range(1,6):
	suma = 0
	for fila in tabla:
		suma = suma + fila[indice_col -1]
	print("La suma de los elementos de la columna %d es %d" %(indice_col,suma))
