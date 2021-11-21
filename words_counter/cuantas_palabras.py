import re

def regex_remplazar_puntuacion(frase):

	nueva_frase = re.sub(r'[,.!¿?;:]', "", frase)

	return nueva_frase

def quitar_puntuacion(frase):

	nueva_frase = [] 
	for palabra in frase:
		if palabra[-1] in ['.',',','!','?',"'",':',';','...']:
			nueva_frase.append(palabra[:-1])
		else:
			nueva_frase.append(palabra)

	return nueva_frase

def crear_mapa(frase):

	d = {}
	for palabra in frase:
		if palabra in d:
			d[palabra] += 1
		else:
			d[palabra] = 1

	return d

def main():

	frase = "Hola como estas tu! Yo muy muy bien, que tal estas tu?".lower().split()
	
	frase_sp = quitar_puntuacion(frase)
	d = crear_mapa(frase_sp)
	print(d)


if __name__ == "__main__":
	main()

