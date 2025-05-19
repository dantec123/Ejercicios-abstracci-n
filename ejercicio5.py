from abc import ABC, abstractmethod

class Empleado(ABC):
    @abstractmethod
    def calcular_sueldo(self):
        pass

class EmpleadoPorHora(Empleado):
    def __init__(self, horas_trabajadas, valor_por_hora):
        self.horas_trabajadas = horas_trabajadas
        self.valor_por_hora = valor_por_hora

    def calcular_sueldo(self):
        return self.horas_trabajadas * self.valor_por_hora

class EmpleadoFijo(Empleado):
    def __init__(self, sueldo_mensual):
        self.sueldo_mensual = sueldo_mensual

    def calcular_sueldo(self):
        return self.sueldo_mensual


empleados = [
    EmpleadoPorHora(150, 1800),
    EmpleadoFijo(300000)
]

for e in empleados:
    print("Sueldo:", e.calcular_sueldo())
