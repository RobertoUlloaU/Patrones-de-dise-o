from __future__ import annotations


class Facade:
    """
    La clase Facade proporciona una interfaz simple para interactuar con subsistemas
    complejos. Se encarga de delegar las solicitudes del cliente a los subsistemas
    apropiados y de gestionar su ciclo de vida.
    """

    def __init__(self, subsystem1: Subsystem1, subsystem2: Subsystem2) -> None:
        """
        Inicializa la fachada con los subsistemas proporcionados. Si no se pasan
        subsistemas, se crean instancias nuevas.
        """
        self._subsystem1 = subsystem1 or Subsystem1()
        self._subsystem2 = subsystem2 or Subsystem2()

    def operation(self) -> str:
        """
        Proporciona un método unificado para realizar operaciones en los subsistemas.
        """
        results = []
        results.append("Fachada inicializa los subsistemas:")
        results.append(self._subsystem1.operation1())
        results.append(self._subsystem2.operation1())
        results.append("Fachada ordena a los subsistemas realizar acciones:")
        results.append(self._subsystem1.operation_n())
        results.append(self._subsystem2.operation_z())
        return "\n".join(results)


class Subsystem1:
    """
    El Subsystem1 representa una parte del sistema complejo. Puede manejar
    solicitudes directamente o a través de la fachada.
    """

    def operation1(self) -> str:
        return "Subsystem1: Listo para iniciar."

    def operation_n(self) -> str:
        return "Subsystem1: Ejecutando acción principal."


class Subsystem2:
    """
    El Subsystem2 representa otra parte del sistema complejo. También puede
    manejar solicitudes directamente o a través de la fachada.
    """

    def operation1(self) -> str:
        return "Subsystem2: Preparándose para iniciar."

    def operation_z(self) -> str:
        return "Subsystem2: Ejecutando acción final."


def client_code(facade: Facade) -> None:
    """
    El código del cliente interactúa con los subsistemas a través de la fachada,
    sin necesidad de conocer los detalles internos de los subsistemas.
    """
    print("Roberto Ulloa\n")  
    print(facade.operation(), end="")


if __name__ == "__main__":
    # Crear instancias de los subsistemas.
    subsystem1 = Subsystem1()
    subsystem2 = Subsystem2()

    # Crear la fachada con los subsistemas.
    facade = Facade(subsystem1, subsystem2)

    # Usar la fachada para realizar operaciones.
    client_code(facade)

