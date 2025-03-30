class AutomovilDinamico:
    """ADT Automóvil con estructura dinámica (lista expandible)."""

    def __init__(self, marca: str, modelo: str):
        """Constructor del automóvil con lista dinámica de ocupantes."""
        self.marca = marca
        self.modelo = modelo
        self.ocupantes = []

    def agregar_ocupante(self, nombre: str) -> None:
        """Agrega un ocupante a la lista dinámica."""
        self.ocupantes.append(nombre)
        print(f"{nombre} ha subido al {self.marca} {self.modelo}.")

    def eliminar_ocupante(self, nombre: str) -> None:
        """Elimina un ocupante si está en la lista."""
        if nombre in self.ocupantes:
            self.ocupantes.remove(nombre)
            print(f"{nombre} ha bajado del auto.")
        else:
            print(" Ocupante no encontrado.")

    def obtener_ocupantes(self) -> list:
        """Devuelve la lista de ocupantes."""
        return self.ocupantes

    def __str__(self) -> str:
        return f" {self.marca} {self.modelo} - Ocupantes: {', '.join(self.ocupantes) if self.ocupantes else 'Vacío'}"


# 🔹 Uso del ADT Automóvil Dinámico
auto_din = AutomovilDinamico("Toyota", "Corolla")
auto_din.agregar_ocupante("Carlos")
auto_din.agregar_ocupante("Maria")
print(auto_din.obtener_ocupantes())
auto_din.eliminar_ocupante("Maria")
print(auto_din)