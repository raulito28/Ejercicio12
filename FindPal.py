class FindPal:
    def __init__(self, PALABRAS, FRASES, archivo, palabras, frases):
        self.PALABRAS = PALABRAS
        self.FRASES = FRASES
        self.archivo = archivo
        self.palabras = palabras
        self.frases = frases
        PALABRAS = "palabras.txt"
        FRASES = "frases.txt"
        archivo = open(PALABRAS, "r")
        palabras = {}
        for linea in archivo:
            palabras[linea.strip()] = []