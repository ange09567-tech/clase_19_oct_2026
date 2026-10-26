class ConexionBaseDatos:
    total_conexiones = 0  # Atributo de Clase

    def __init__(self, db_name: str):
        self.db_name = db_name  # Atributo de Instancia
        ConexionBaseDatos.total_conexiones += 1

if __name__ == "__main__":
    c1 = ConexionBaseDatos("Ventas")
    c2 = ConexionBaseDatos("Inventario")
    print(f"Total de conexiones creadas: {ConexionBaseDatos.total_conexiones}")  # Imprime: 2