class Nodo:
    def __init__(self, valor):
        self._valor = valor  # Atributo privado
        self._izquierdo = None
        self._derecho = None

    # Getter y Setter para el valor
    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, valor):
        self._valor = valor

    # Getter y Setter para el hijo izquierdo
    @property
    def izquierdo(self):
        return self._izquierdo

    @izquierdo.setter
    def izquierdo(self, nodo):
        self._izquierdo = nodo

    # Getter y Setter para el hijo derecho
    @property
    def derecho(self):
        return self._derecho

    @derecho.setter
    def derecho(self, nodo):
        self._derecho = nodo


class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if not self.raiz:
            self.raiz = Nodo(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izquierdo is None:
                nodo.izquierdo = Nodo(valor)
            else:
                self._insertar_recursivo(nodo.izquierdo, valor)
        else:
            if nodo.derecho is None:
                nodo.derecho = Nodo(valor)
            else:
                self._insertar_recursivo(nodo.derecho, valor)

    def buscar(self, valor):
        return self._buscar_recursivo(self.raiz, valor)

    def _buscar_recursivo(self, nodo, valor):
        if nodo is None:
            return False
        if nodo.valor == valor:
            return True
        elif valor < nodo.valor:
            return self._buscar_recursivo(nodo.izquierdo, valor)
        else:
            return self._buscar_recursivo(nodo.derecho, valor)

    def es_hoja(self, nodo):
        return nodo.izquierdo is None and nodo.derecho is None

    def altura(self):
        return self._altura_recursiva(self.raiz)

    def _altura_recursiva(self, nodo):
        if nodo is None:
            return -1
        altura_izq = self._altura_recursiva(nodo.izquierdo)
        altura_der = self._altura_recursiva(nodo.derecho)
        return 1 + max(altura_izq, altura_der)

    def cantidad(self):
        return self._cantidad_recursiva(self.raiz)

    def _cantidad_recursiva(self, nodo):
        if nodo is None:
            return 0
        return 1 + self._cantidad_recursiva(nodo.izquierdo) + self._cantidad_recursiva(nodo.derecho)

    def amplitud(self):
        if not self.raiz:
            return 0
        nivel = [self.raiz]
        max_amplitud = 0
        while nivel:
            max_amplitud = max(max_amplitud, len(nivel))
            siguiente_nivel = []
            for nodo in nivel:
                if nodo.izquierdo:
                    siguiente_nivel.append(nodo.izquierdo)
                if nodo.derecho:
                    siguiente_nivel.append(nodo.derecho)
            nivel = siguiente_nivel
        return max_amplitud


# Ejemplo
if __name__ == "__main__":
    arbol = ArbolBinario()
    arbol.insertar(10)
    arbol.insertar(5)
    arbol.insertar(15)
    arbol.insertar(3)
    arbol.insertar(7)

    # Buscar
    print("Buscar 15:", arbol.buscar(15))  # verdad
    print("Buscar 20:", arbol.buscar(20))  # Falso

    # EsHoja
    print("Es hoja el nodo con valor 3:", arbol.es_hoja(arbol.raiz.izquierdo.izquierdo))  # verdad

    # Acceder a través de getter y setter
    print("Valor de la raíz:", arbol.raiz.valor)  # 10
    arbol.raiz.valor = 24
    print("Nuevo valor de la raíz:", arbol.raiz.valor)  # 24

    # Altura
    print("Altura del árbol:", arbol.altura())  # 2

    # Cantidad
    print("Cantidad de nodos:", arbol.cantidad())  # 5

    # Amplitud
    print("Amplitud del árbol:", arbol.amplitud())  # 2
