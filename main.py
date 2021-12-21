import FindPal as sd
print("Lista de palabras: \n", palabras)

archivo = open(FRASES, "r")
frases = []
for frase in archivo:
    frases.append(frase.strip())
    for palabra in palabras:
        palabras[palabra].append(frase.lower().count(palabra))
archivo.close()
print("Frases: \n", frases)
print("Palabras en frases: \n", palabras)