class NodoAVL:
    def __init__(self, key, height=1, left=None, right=None):
        self.key = key
        self.height = height
        self.left = left
        self.right = right

class ArbolAVL:
    def obtener_altura(self, nodo):
        return nodo.height if nodo else 0

    def obtener_balance(self, nodo):
        return self.obtener_altura(nodo.left) - self.obtener_altura(nodo.right) if nodo else 0

    def rotar_derecha(self, y):
        x = y.left
        T2 = x.right
        
        x.right = y
        y.left = T2
        
        y.height = max(self.obtener_altura(y.left), self.obtener_altura(y.right)) + 1
        x.height = max(self.obtener_altura(x.left), self.obtener_altura(x.right)) + 1
        
        return x

    def rotar_izquierda(self, x):
        y = x.right
        T2 = y.left
        
        y.left = x
        x.right = T2
        
        x.height = max(self.obtener_altura(x.left), self.obtener_altura(x.right)) + 1
        y.height = max(self.obtener_altura(y.left), self.obtener_altura(y.right)) + 1
        
        return y

    def insertar(self, nodo, key):
        if not nodo:
            return NodoAVL(key)
        
        if key < nodo.key:
            nodo.left = self.insertar(nodo.left, key)
        else:
            nodo.right = self.insertar(nodo.right, key)
        
        nodo.height = max(self.obtener_altura(nodo.left), self.obtener_altura(nodo.right)) + 1
        balance = self.obtener_balance(nodo)
        
        if balance > 1 and key < nodo.left.key:
            return self.rotar_derecha(nodo)
        if balance < -1 and key > nodo.right.key:
            return self.rotar_izquierda(nodo)
        if balance > 1 and key > nodo.left.key:
            nodo.left = self.rotar_izquierda(nodo.left)
            return self.rotar_derecha(nodo)
        if balance < -1 and key < nodo.right.key:
            nodo.right = self.rotar_derecha(nodo.right)
            return self.rotar_izquierda(nodo)
        
        return nodo

    def pre_orden(self, nodo):
        if nodo:
            print(nodo.key, end=" ")
            self.pre_orden(nodo.left)
            self.pre_orden(nodo.right)

if __name__ == "__main__":
    arbol = ArbolAVL()
    raiz = None
    valores = [10, 20, 30, 40, 50, 25]
    
    for v in valores:
        raiz = arbol.insertar(raiz, v)
    
    print("Recorrido en pre-orden del árbol AVL:")
    arbol.pre_orden(raiz)