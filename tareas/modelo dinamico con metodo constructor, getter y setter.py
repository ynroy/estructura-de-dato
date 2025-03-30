class AutomovilDinamico:
    """ADT Automóvil con estructura dinámica (lista expandible)."""

    def __init__(self, marca: str, modelo: str, año: int):
        """Constructor para automóvil con lista dinámica de ocupantes."""
        self.año = año
        self.marca = marca
        self.modelo = modelo
        self.ocupantes = []  # Lista dinámica para los ocupantes
    # Getter para obtener el año
    def get_año(self) -> int:
        return self.año

    # Getter para obtener la marca
    def get_marca(self) -> str:
        return self.marca
    
    # Setter para cambiar el año
    def set_año(self, nuevo_año: int) -> None:
        if isinstance(nuevo_año, int) and nuevo_año > 1885:  # El año debe ser mayor a 1885 (primer automóvil)
            self.año = nuevo_año
        else:
            print(" Año inválido.")

    # Setter para cambiar la marca
    def set_marca(self, nueva_marca: str) -> None:
        if isinstance(nueva_marca, str) and len(nueva_marca) > 1:
            self.marca = nueva_marca
        else:
            print(" La marca debe ser un nombre válido.")

    # Getter para obtener el modelo
    def get_modelo(self) -> str:
        return self.modelo

    # Setter para cambiar el modelo
    def set_modelo(self, nuevo_modelo: str) -> None:
        if isinstance(nuevo_modelo, str) and len(nuevo_modelo) > 1:
            self.modelo = nuevo_modelo
        else:
            print(" El modelo debe ser un nombre válido.")

    # Método para agregar un ocupante
    def agregar_ocupante(self, nombre: str) -> None:
        self.ocupantes.append(nombre)
        print(f"{nombre} ha subido al {self.marca} {self.modelo}.")

    # Método para eliminar un ocupante
    def eliminar_ocupante(self, nombre: str) -> None:
        if nombre in self.ocupantes:
            self.ocupantes.remove(nombre)
            print(f"{nombre} ha bajado del auto.")
        else:
            print(f" {nombre} no está en el auto.")

    def __str__(self) -> str:
        return f"{self.marca} {self.modelo} - Ocupantes: {', '.join(self.ocupantes) if self.ocupantes else 'Vacío'}"

# Uso del ADT Automóvil Dinámico
auto_din = AutomovilDinamico("Toyota", "Corolla", "1993")
auto_din.agregar_ocupante("Carlos")
auto_din.agregar_ocupante("María")
print(auto_din)  # Imprime la información completa
auto_din.eliminar_ocupante("Carlos")
print(auto_din)  # Imprime la información actualizada
print(f"Año: {auto_din.get_año()}")