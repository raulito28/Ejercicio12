class FindPal:
    def __init__(self, PALABRAS, FRASES, archivo, palabras, frases):
        self.PALABRAS = PALABRAS
        self.FRASES = FRASES
        self.archivo = archivo
        self.palabras = palabras
        self.frases = frases
"""Cuenta palabras en frases"""
PALABRAS = "palabras.txt"
FRASES = "frases.txt"
archivo = open(PALABRAS, "r")
palabras = {}
for linea in archivo:
    palabras[linea.strip()] = []
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