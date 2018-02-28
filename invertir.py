class Lenguaje():
    palabras = []
    contador = 0
    lista2 = []
    sw = 0

    """docstring for Lenguaje"""

    def invertir(self, cadena):
        aux = list(cadena)
        aux.remove("{")
        aux.remove("}")
        cadena = "".join(aux)

        self.palabras = cadena.split(",")

        aux = self.palabras
        for palabra in aux:
            self.palabras[self.contador] = palabra[::-1] + ","
            self.contador = self.contador + 1
            aux = self.palabras[self.contador - 1]
        temp = len(aux)
        self.palabras[self.contador - 1] = aux[:temp - 1]

        self.palabras.append("}")
        self.palabras.insert(0, "{")

        cadena1 = "".join(self.palabras)

        print(cadena1)


print("digite el lenguaje ENTRE COMILLAS \n")

st = input()


leng = Lenguaje()
leng.invertir(st)
