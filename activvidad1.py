class Estudiante:
    def __init__(self, nombre: str):
        self._nombre = nombre
        self._notas: list[float] = []

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def notas(self) -> list[float]:
        # Se retorna una copia de la lista para evitar mutabilidad no deseada desde el exterior
        return self._notas.copy()

    def agregar_nota(self, nota: float) -> None:
        """Agrega una nota si se encuentra en el rango válido de 0.0 a 5.0."""
        if 0.0 <= nota <= 5.0:
            self._notas.append(nota)
            print(f"Nota {nota} agregada correctamente a {self._nombre}.")
        else:
            print(f"Error: La nota {nota} no es válida. Debe estar entre 0.0 y 5.0.")

    def calcular_promedio(self) -> float:
        """Calcula el promedio de las notas registradas."""
        if not self._notas:
            return 0.0
        return sum(self._notas) / len(self._notas)


# --- PRUEBA DE EJECUCIÓN ---
if __name__ == "__main__":
    print("=== EJERCICIO 1: SISTEMA DE CALIFICACIONES ===")
    estudiante = Estudiante("Jose Meriño")
    
    # Intentos de agregar notas
    estudiante.agregar_nota(4.5)
    estudiante.agregar_nota(3.8)
    estudiante.agregar_nota(5.0)
    estudiante.agregar_nota(-1.0)  # Nota inválida
    estudiante.agregar_nota(6.0)   # Nota inválida

    print(f"\nNotas de {estudiante.nombre}: {estudiante.notas}")
    print(f"Promedio general: {estudiante.calcular_promedio():.2f}")