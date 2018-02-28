class Lenguaje():
    palabras = []
    contador = 0
    lista2 = []
    """docstring for Lenguaje"""

    def invertir(self, cadena):
        aux = list(cadena)
        aux.remove("{")
        aux.remove("}")
        cadena = "".join(aux)

        self.palabras = cadena.split(",")
        print(self.palabras)
        aux = self.palabras
        for palabra in aux:
            self.palabras[self.contador] = palabra[::-1]
            self.contador = self.contador + 1

        for x in range(1, self.contador, 1):
            self.palabras.insert(x, ",")

        self.palabras.append("}")
        self.palabras.insert(0, "{")

        cadena1 = "".join(self.palabras)

        print(cadena1)


print("digite el lenguaje entre comillas \n")

st = input()


leng = Lenguaje()
leng.invertir(st)
