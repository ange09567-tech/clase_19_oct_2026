class TarjetaCredito:
    def __init__(self, titular: str, numero_tarjeta: str):
        self.titular = titular
        self.numero_tarjeta = numero_tarjeta

    def calcular_cashback(self, monto: float) -> float:
        """Método base que será sobreescrito por las subclases."""
        return 0.0


class TarjetaGold(TarjetaCredito):
    def calcular_cashback(self, monto: float) -> float:
        # Retorna el 2% del monto de compra
        return monto * 0.02


class TarjetaBlack(TarjetaCredito):
    def calcular_cashback(self, monto: float) -> float:
        # Retorna el 5% del monto de compra
        return monto * 0.05


# Función polimórfica para procesar compras en cualquier tarjeta
def procesar_compra(tarjeta: TarjetaCredito, monto: float):
    cashback = tarjeta.calcular_cashback(monto)
    print(f"Titular: {tarjeta.titular} | Tarjeta: {tarjeta.__class__.__name__}")
    print(f"  -> Monto de la compra: ${monto:,.2f}")
    print(f"  -> Cashback acumulado: ${cashback:,.2f}\n")


# --- PRUEBA DE EJECUCIÓN ---
if __name__ == "__main__":
    print("=== EJERCICIO 2: SIMULADOR DE TARJETAS DE CRÉDITO ===")
    
    tarjeta_gold = TarjetaGold("Jose Meriño", "4500-1234-5678-9012")
    tarjeta_black = TarjetaBlack("Yume", "5200-9876-5432-1098")

    monto_compra = 250000.0  # $250,000 COP

    # Invocación polimórfica
    procesar_compra(tarjeta_gold, monto_compra)
    procesar_compra(tarjeta_black, monto_compra)