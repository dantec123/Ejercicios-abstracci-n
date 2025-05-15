class Vehiculo(ABC):
    @abstractmethod
    def mover(self):
        pass

    @abstractmethod
    def detener(self):
        pass

class Coche(Vehiculo):
    def mover(self):
        return "El coche está en movimiento."

    def detener(self):
        return "El coche se ha detenido."

class Bicicleta(Vehiculo):
    def mover(self):
        return "La bicicleta está en movimiento."
 
    def detener(self):
        return "La bicicleta se ha detenido."

