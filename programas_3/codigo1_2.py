#este programa practica el uso de open() como un iterable

from os import strerror

try:
	ccnt = lcnt = 0

	for line in open('/home/rodrigo/Escritorio/curso_python/documento_1', 'rt'):
		lcnt += 1
		for ch in line:
			print(ch, end='')
			ccnt += 1
	print("\n\nCaracteres en el archivo: ", ccnt)
	print("Lineas en el archivo:     ", lcnt)

except IOError as e:
	print("Se produjo un error de E/S: ", strerror(e.errno))
