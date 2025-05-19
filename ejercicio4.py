from abc import ABC, abstractmethod

class Notificacion(ABC):
    @abstractmethod
    def enviar(self, mensaje):
        pass

class Email(Notificacion):
    def enviar(self, mensaje):
        print("Enviando email con mensaje:", mensaje)

class SMS(Notificacion):
    def enviar(self, mensaje):
        print("Enviando SMS con mensaje:", mensaje)


notificaciones = [Email(), SMS()]
for n in notificaciones:
    n.enviar("hola")
