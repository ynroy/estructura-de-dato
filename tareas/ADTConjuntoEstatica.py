class ConjuntoEstatico:
    def __init__(self, capacidad=10):
        self.capacidad = capacidad
        self.elementos = [None] * capacidad
        self.tamanio = 0

    def get_tamanio(self):
        return self.tamanio

    def get_elemento(self, indice):
        if 0 <= indice < self.tamanio:
            return self.elementos[indice]
        raise IndexError("Índice fuera de rango")

    def agregar_elemento(self, valor):
        if not self.existe(valor):
            if self.tamanio < self.capacidad:
                self.elementos[self.tamanio] = valor
                self.tamanio += 1
            else:
                print("El conjunto está lleno (estático).")
        else:
            print("El elemento ya existe en el conjunto.")

    def eliminar_elemento(self, valor):
        for i in range(self.tamanio):
            if self.elementos[i] == valor:
                for j in range(i, self.tamanio - 1):
                    self.elementos[j] = self.elementos[j + 1]
                self.elementos[self.tamanio - 1] = None
                self.tamanio -= 1
                return
        print("Elemento no encontrado.")

    def existe(self, valor):
        return valor in self.elementos[:self.tamanio]

    def mostrar(self):
        print("{", end=" ")
        for i in range(self.tamanio):
            print(self.elementos[i], end=", " if i < self.tamanio - 1 else "")
        print("}")
# Prueba con estructura estática
print("Conjunto Estático:")
conj_est = ConjuntoEstatico(5)
conj_est.agregar_elemento(1)
conj_est.agregar_elemento(2)
conj_est.agregar_elemento(3)
conj_est.mostrar()
conj_est.eliminar_elemento(2)
conj_est.mostrar()