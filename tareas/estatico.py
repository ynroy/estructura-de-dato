class AutomovilEstatico:
    """ADT Automóvil con estructura estática (lista fija)."""

    def __init__(self, marca: str, modelo: str, capacidad: int = 2):
        """Constructor con capacidad fija para ocupantes."""
        self.marca = marca
        self.modelo = modelo
        self.capacidad = capacidad
        self.ocupantes = [None] * capacidad  # Lista de tamaño fijo

    def agregar_ocupante(self, nombre: str, posicion: int) -> None:
        """Agrega un ocupante en una posición específica."""
        if 0 <= posicion < self.capacidad and self.ocupantes[posicion] is None:
            self.ocupantes[posicion] = nombre
            print(f"{nombre} añadido en la posición {posicion}.")
        else:
            print(" Posición ocupada o inválida.")

    def obtener_ocupante(self, posicion: int) -> str:
        """Obtiene el nombre de un ocupante en una posición."""
        if 0 <= posicion < self.capacidad:
            return self.ocupantes[posicion] or "Vacío"
        return "Posición inválida."

    def __str__(self) -> str:
        return f" {self.marca} {self.modelo} - Ocupantes: {self.ocupantes}"


# 🔹 Uso del ADT Automóvil Estático
auto = AutomovilEstatico("Suzuki", "Baleno")
auto.agregar_ocupante("Alberto", 0)
auto.agregar_ocupante("Josefina", 1)
print(auto.obtener_ocupante(1))
print(auto)