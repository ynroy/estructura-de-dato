class ConjuntoDinamico:
    def __init__(self):
        self.elementos = []

    def get_tamanio(self):
        return len(self.elementos)

    def get_elemento(self, indice):
        if 0 <= indice < len(self.elementos):
            return self.elementos[indice]
        raise IndexError("Índice fuera de rango")

    def agregar_elemento(self, valor):
        if not self.existe(valor):
            self.elementos.append(valor)
        else:
            print("El elemento ya existe en el conjunto.")

    def eliminar_elemento(self, valor):
        if valor in self.elementos:
            self.elementos.remove(valor)
        else:
            print("Elemento no encontrado.")

    def existe(self, valor):
        return valor in self.elementos

    def mostrar(self):
        print("{", end=" ")
        print(", ".join(str(x) for x in self.elementos), end=" ")
        print("}")
# Prueba con estructura dinámica
print("\nConjunto Dinámico:")
conj_din = ConjuntoDinamico()
conj_din.agregar_elemento(10)
conj_din.agregar_elemento(20)
conj_din.agregar_elemento(30)
conj_din.mostrar()
conj_din.eliminar_elemento(10)
conj_din.mostrar()