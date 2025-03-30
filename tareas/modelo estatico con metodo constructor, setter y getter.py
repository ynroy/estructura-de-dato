class AutomovilEstatico:
    """ADT Automóvil con estructura estática."""

    def __init__(self, marca: str, modelo: str, capacidad: int = 2):
        """Constructor con capacidad fija para ocupantes."""
        self.marca = marca
        self.modelo = modelo
        self.capacidad = capacidad
        self.ocupantes = [None] * capacidad  # Lista de tamaño fijo

    # Getter para obtener la marca
    def get_marca(self) -> str:
        return self.marca

    # Setter para cambiar la marca
    def set_marca(self, nueva_marca: str) -> None:
        if isinstance(nueva_marca, str) and len(nueva_marca) > 1:
            self.marca = nueva_marca
        else:
            print("⚠️ La marca debe ser un nombre válido.")

    # Getter para obtener el modelo
    def get_modelo(self) -> str:
        return self.modelo

    # Setter para cambiar el modelo
    def set_modelo(self, nuevo_modelo: str) -> None:
        if isinstance(nuevo_modelo, str) and len(nuevo_modelo) > 1:
            self.modelo = nuevo_modelo
        else:
            print("⚠️ El modelo debe ser un nombre válido.")

    # Getter para obtener un ocupante en una posición específica
    def obtener_ocupante(self, posicion: int) -> str:
        if 0 <= posicion < self.capacidad:
            return self.ocupantes[posicion] or "Vacío"
        return "⚠️ Posición inválida."

    # Setter para agregar un ocupante en una posición específica
    def agregar_ocupante(self, nombre: str, posicion: int) -> None:
        if 0 <= posicion < self.capacidad and self.ocupantes[posicion] is None:
            self.ocupantes[posicion] = nombre
            print(f"{nombre} añadido en la posición {posicion}.")
        else:
            print("⚠️ Posición ocupada o inválida.")

    def __str__(self) -> str:
        return f"{self.marca} {self.modelo} - Ocupantes: {self.ocupantes}"

# Uso del ADT Automóvil Estático
auto = AutomovilEstatico("Suzuki", "Baleno")
auto.agregar_ocupante("Alberto", 0)
auto.agregar_ocupante("Josefina", 1)
print(auto.obtener_ocupante(1))  # Imprime "Josefina"
print(auto)  # Imprime la información completa