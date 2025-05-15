from abc import ABC, abstractmethod

class Pago(ABC):
    @abstractmethod
    def procesar_pago(self, monto):
        pass


class TarjetaCredito(Pago):
    def procesar_pago(self, monto):
        print(f"Procesando pago de ${monto} con tarjeta de crédito.")


class PayPal(Pago):
    def procesar_pago(self, monto):
        print(f"Procesando pago de ${monto} a través de PayPal.")


def realizar_pago(pago: Pago, monto: float):
    pago.procesar_pago(monto)


tarjeta = TarjetaCredito()
paypal = PayPal()

realizar_pago(tarjeta, 100.50)
realizar_pago(paypal, 200.75)
